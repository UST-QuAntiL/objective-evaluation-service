![Tests passed](https://github.com/UST-QuAntiL/objective-function-service/actions/workflows/test.yml/badge.svg)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![codecov](https://codecov.io/gh/UST-QuAntiL/objective-function-service/branch/main/graph/badge.svg?token=YZY0AA6LCJ)](https://codecov.io/gh/UST-QuAntiL/objective-function-service)


# Objective function service

The objective function service enables a service-based evaluation of quantum execution results for variational quantum algorithms (VQA).

It implements multiple cost and objective functions commonly employed in current quantum applications.
* Cost functions are used to determine the quality of a bitstring measured on a quantum computer. These functions are problem-specific, e.g., Traveling Sales Person (TSP) or Maximum Cut (MaxCut), and are required to further process the quantum measurement.
* Objective functions are used for the parameter optimization of VQAs. They summarize the overall quality of all measured solutions in one single number, the so-called objective value.
The objective values is used by optimizers (see [here](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html)) to determine new parameter values that aim to improve the objective value and thus the overall solution quality.
Therefore objective functions heavily influence the optimization process (see [here](https://www.mdpi.com/2079-9292/11/7/1033/htm) for more details). 
Examples are: expectation value, [CVaR](https://quantum-journal.org/papers/q-2020-04-20-256/), or [Gibbs](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.2.023074)

Additionally, the objective function service contains a visualization module, enabling generation of an image representing the visualization of the execution result's most occurring bitstring.
For example, for the TSP problem, the route taken by the solution is highlighted in the graph.


## Running the Application
The easiest way to get start is using a pre-built Docker image: ``docker run -p 5072:5072 planqk/objective-function-service``

Alternatively, the application can be built manually:
1. Clone the repository using ``git clone https://github.com/UST-QuAntiL/objective-function-service.git``
2. Navigate to the repository  ``cd objective-function-service``
3. Build the Docker container: ``docker build -t objective-function-service .``
4. Run the Docker container: ``docker run -p 5072:5072 objective-function-service``

Then the application can be accessed via: [http://127.0.0.1:5072](http://127.0.0.1:5072).

## API Documentation

The objective function service provides a Swagger UI, specifying the request schemas and showcasing exemplary requests for all API endpoints.
 * Swagger UI: [http://127.0.0.1:5072/app/swagger-ui](http://127.0.0.1:5072/app/swagger-ui).



## Developer Guide

### Setup (exemplary for ubuntu 18.04): 
* ``git clone https://github.com/UST-QuAntiL/objective-function-service.git`` 
* ``cd objective-function-service``
* ``sudo -H pip install virtualenv`` (if you don't have virtualenv installed)
* ``virtualenv venv`` (create virtualenv named 'venv')
* ``source venv/bin/activate`` (enter virtualenv; in Windows systems activate might be in ``venv/Scripts``)
* ``pip install -r requirements.txt`` (install application requirements)

### Execution:
* Run the application with: ``flask run --port=5072``
* Test with: ``python -m unittest discover``
* Coverage with: ``coverage run --branch --include 'app/*' -m unittest discover; coverage report``

### Codestyle: 
``black .`` OR ``black FILE|DIRECTORY``

## Disclaimer of Warranty
Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

## Haftungsausschluss
Dies ist ein Forschungsprototyp. Die Haftung für entgangenen Gewinn, Produktionsausfall, Betriebsunterbrechung, entgangene Nutzungen, Verlust von Daten und Informationen, Finanzierungsaufwendungen sowie sonstige Vermögens- und Folgeschäden ist, außer in Fällen von grober Fahrlässigkeit, Vorsatz und Personenschäden, ausgeschlossen.