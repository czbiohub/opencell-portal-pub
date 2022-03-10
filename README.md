# OpenCell web portal
This is a public read-only repo for the OpenCell database and web app.

*This is a public snapshot of the OpenCell repo without test data, deployment scripts, or database credentials. It is meant to document the database schema, data processing methodology, and the architecture of the OpenCell web app as described in our [2022 publication](https://www.science.org/doi/10.1126/science.abi6983) ([preprint here](https://www.biorxiv.org/content/10.1101/2021.03.29.437450v2)).*


## Directories
 - `opencell`: this is a Python package that contains data ingestion and processing methods, database models, and the backend REST API
 - `client`: this is the frontend (a React app)
- `deploy/local`: local staging deployment


## License
Chan Zuckerberg Biohub Software License

This software license is the 2-clause BSD license plus a third clause
that prohibits redistribution and use for commercial purposes without further
permission.

Copyright © 2020-2022. Chan Zuckerberg Biohub.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1.	Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.

2.	Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

3.	Redistributions and use for commercial purposes are not permitted without
the Chan Zuckerberg Biohub's written permission. For purposes of this license,
commercial purposes are the incorporation of the Chan Zuckerberg Biohub's
software into anything for which you will charge fees or other compensation or
use of the software to perform a commercial service for a third party.
Contact ip@czbiohub.org for commercial licensing opportunities.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
