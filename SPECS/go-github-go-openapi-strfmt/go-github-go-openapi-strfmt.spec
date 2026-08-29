# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           strfmt
%define go_import_path  github.com/go-openapi/strfmt

# The optional MongoDB integration (enable/mongodb) imports the unpackaged
# go.mongodb.org/mongo-driver and is not used by Prometheus (strfmt's core
# uses its internal bsonlite). Exclude it; all other tests still run.
%global go_test_exclude_glob */enable/mongodb*

Name:           go-github-go-openapi-strfmt
Version:        0.26.2
Release:        %autorelease
Summary:        openapi toolkit common string formats
License:        Apache-2.0
URL:            https://github.com/go-openapi/strfmt
#!RemoteAsset:  sha256:8876b50b7893769233c0786ec9933b5160260154f61a9b58ecca84c0cf926cc7
Source0:        https://github.com/go-openapi/strfmt/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-openapi/errors)
BuildRequires:  go(github.com/go-openapi/testify/v2)
BuildRequires:  go(github.com/go-viper/mapstructure/v2)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/oklog/ulid/v2)
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/go-openapi/strfmt) = %{version}
Provides:       go(github.com/go-openapi/strfmt/conv) = %{version}
Provides:       go(github.com/go-openapi/strfmt/internal/bsonlite) = %{version}

Requires:       go(github.com/go-openapi/errors)
Requires:       go(github.com/go-viper/mapstructure/v2)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/oklog/ulid/v2)
Requires:       go(golang.org/x/net)

%description
This package provides a set of OpenAPI/Swagger string-format helpers
(date-time, UUID, email, URI, MAC, …) used across the go-openapi
projects for marshalling and validating typed string values.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
