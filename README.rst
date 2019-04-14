============================
stepfunctions-describe-execution-task
============================

.. _APL2: http://www.apache.org/licenses/LICENSE-2.0.txt

Describes an AWS step-function execution

AWS Permissions Required
------------------------
- states:DescribeExecution

Handler Method
--------------
.. code::

  function.handler

Request Syntax
--------------
.. code::

    {
        "executionArn": "arn",
    }

**executionArn**
    The Amazon Resource Name (ARN) of the execution to describe - REQUIRED

Response syntax
---------------

.. code::

    {
        'executionArn': 'string',
        'stateMachineArn': 'string',
        'name': 'string',
        'status': 'RUNNING'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'ABORTED',
        'startDate': 'iso8601 date/time',
        'stopDate': 'iso8601 date/time',
        'input': 'string',
        'output': 'string'
    }

Lambda Package Location
-----------------------
https://s3.amazonaws.com/lambdalambdalambda-repo/quinovas/stepfunctions-describe-execution-task/stepfunctions-describe-execution-task-0.0.1.zip

License: `APL2`_
