# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname griffe

Name:           python-%{srcname}
Version:        2.0.2
Release:        %autorelease
Summary:        Signatures for entire Python programs
License:        ISC
URL:            https://github.com/mkdocstrings/griffe
BuildArch:      noarch

Requires:       python3dist(griffecli) = %{version}
Requires:       python3dist(griffelib) = %{version}

Provides:       python3-%{srcname} = %{version}-%{release}
# This is a meta package, so %python_provide is not applicable here.
Provides:       python3dist(%{srcname}) = %{version}

%description
Signatures for entire Python programs. Extract the structure, the frame, the
skeleton of your project, to generate API documentation or find breaking
changes in your API. This is a meta-package that pulls in griffelib (core
library) and griffecli (command-line interface).

%files

%changelog
%autochangelog
