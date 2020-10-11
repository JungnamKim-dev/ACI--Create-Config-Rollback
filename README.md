# ACI--Create-Config-Rollback

This simple script will create a config rollback point on your APIC. It's an ideal starting module for any APIC automation scripts because it creates a cookie to use in all subsequents POSTs and there's that rollback point if your change goes south.

![Here be screengrab](https://github.com/mrdavehill/ACI--Create-Config-Rollback/blob/main/APICSnapshot.jpg)
 
## Use Case Description

Dev.

Test code and easily back any changes out. Update, rinse, repeat.

Prod.

Create a rollback as a first step in any script and reference the change record number. CAB will love you.

## Installation

Clone to your machine, update credentials.py, run APICSnapshot.py.

## Configuration

credentials.py

host = 'https://myapic.example.com'
username = 'admin'
password = 'QWer1234'

## Usage

There's an example of this script in one of my projects that [creates EPGs, BDs and Vlan pools.](https://github.com/mrdavehill/ACI---Add-BD-EPG-and-Vlan-Pool/blob/main/APICImporter.py)

### DevNet Sandbox

A great way to make your repo easy for others to use is to provide a link to a [DevNet Sandbox](https://developer.cisco.com/site/sandbox/) that provides a network or other resources required to use this code. In addition to identifying an appropriate sandbox, be sure to provide instructions and any configuration necessary to run your code with the sandbox.

## How to test the software

Provide details on steps to test, versions of components/dependencies against which code was tested, date the code was last tested, etc. 
If the repo includes automated tests, detail how to run those tests.
If the repo is instrumented with a continuous testing framework, that is even better.


## Known issues

Document any significant shortcomings with the code. If using [GitHub Issues](https://help.github.com/en/articles/about-issues) to track issues, make that known and provide any templates or conventions to be followed when opening a new issue. 

## Getting help

Instruct users how to get help with this code; this might include links to an issues list, wiki, mailing list, etc.

**Example**

If you have questions, concerns, bug reports, etc., please create an issue against this repository.

## Getting involved

This section should detail why people should get involved and describe key areas you are currently focusing on; e.g., trying to get feedback on features, fixing certain bugs, building important pieces, etc. Include information on how to setup a development environment if different from general installation instructions.

General instructions on _how_ to contribute should be stated with a link to [CONTRIBUTING](./CONTRIBUTING.md) file.

## Author(s)

This project was written and is maintained by the following individuals:

* Dave Hill <dave@davehill.org>
