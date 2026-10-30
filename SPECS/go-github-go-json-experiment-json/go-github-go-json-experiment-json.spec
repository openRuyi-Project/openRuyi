# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           json
%define go_import_path  github.com/go-json-experiment/json
%define commit          c27c302e5fc3f63878d1faaf2971f132bae3b152

Name:           go-github-go-json-experiment-json
Version:        0+git20261023.c27c302e5fc3
Release:        %autorelease
Summary:        Experimental JSON implementation for Go
License:        BSD-3-Clause
URL:            https://github.com/go-json-experiment/json
#!RemoteAsset:  sha256:44d53e0948949924acf32292f086613dba95bde18252d59eab375276a5d24bba
Source0:        https://github.com/go-json-experiment/json/archive/%{commit}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit}

BuildRequires:  go >= 1.26
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/internal) = %{version}
Provides:       go(%{go_import_path}/internal/jsonflags) = %{version}
Provides:       go(%{go_import_path}/internal/jsonopts) = %{version}
Provides:       go(%{go_import_path}/internal/jsontest) = %{version}
Provides:       go(%{go_import_path}/internal/jsonwire) = %{version}
Provides:       go(%{go_import_path}/internal/zstd) = %{version}
Provides:       go(%{go_import_path}/jsontext) = %{version}
Provides:       go(%{go_import_path}/v1) = %{version}

%description
This experimental JSON implementation explores APIs for a future version
of Go's encoding/json package. It includes JSON text processing, the v1
compatibility package, and the complete upstream tests and test data.

%files
%doc README.md AUTHORS CONTRIBUTORS
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
