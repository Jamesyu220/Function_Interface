# coding=utf-8
# Copyright 2018-2023 EvaDB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import numpy as np
import pandas as pd

from evadb.catalog.catalog_type import NdArrayType
from evadb.functions.abstract.abstract_function import AbstractFunction
from evadb.functions.decorators.decorators import forward
from evadb.functions.decorators.io_descriptors.data_types import PandasDataframe


class DescribeFunction(AbstractFunction):
    @property
    def name(self) -> str:
        return "DescribeFunction"
    
    def setup(self) -> None:
        pass 

    @forward(
        input_signatures=[
            PandasDataframe(
                columns=["module", "function"],
                column_types=[
                    NdArrayType.STR,
                    NdArrayType.STR
                ],
                column_shapes=[(1,), (1,)],
            )
        ],
        output_signatures=[
            PandasDataframe(
                columns=["param_name", "param_type", "return_type"],
                column_types=[
                    NdArrayType.STR,
                    NdArrayType.STR,
                    NdArrayType.STR
                ],
                column_shapes=[(None,), (None,), (None,)],
            )
        ],
    )
    def forward(self, text_df):
        import importlib
        import inspect

        def get_function_info(text_df: PandasDataframe):
            module_name = text_df['module'][0]
            function_name = text_df['function'][0]

            # debug
            print(f"module: {module_name}")
            print(f"function: {function_name}")
            # debug

            try:
                module = importlib.import_module(module_name)

                # Use getattr to retrieve the function by name
                if hasattr(module, function_name) and callable(getattr(module, function_name)):
                    func = getattr(module, function_name)
                else:
                    raise ImportError(f"Function {function_name} Not Found")

            except ImportError:
                print(f"Module {module_name} not found")

            signature = inspect.signature(func)
            parameters = signature.parameters
            return_type = np.array([signature.return_annotation] + [np.nan] * (len(parameters) - 1))

            # Extract parameter names and types
            param_name = np.array([param for param in parameters])
            param_type = np.array([parameters[param].annotation for param in parameters])

            # debug
            print(f"param_name: {param_name}")
            print(f"param_type: {param_type}")
            print(f"return_type: {return_type}")
            # debug

            return param_name, param_type, return_type

        param_name, param_type, return_type = get_function_info(text_df = text_df)

        # debug
        print("successfully get the values!")
        # debug

        df = pd.DataFrame({"param_name": param_name, "param_type": param_type, "return_type": return_type})

        # debug
        print("successfully get the df!")
        # debug
                
        return df
