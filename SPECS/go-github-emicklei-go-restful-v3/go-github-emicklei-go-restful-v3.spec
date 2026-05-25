# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-restful
%define go_import_path  github.com/emicklei/go-restful/v3
# These examples require optional dependencies that are not part of the library
# dependency path, such as gorilla/schema, httpin, jwt, msgpack, and openapi.
# - HNO3Miracle
%define go_test_exclude_glob %{shrink:
    github.com/emicklei/go-restful/v3/examples/form*
    github.com/emicklei/go-restful/v3/examples/jwtauth
    github.com/emicklei/go-restful/v3/examples/msgpack
    github.com/emicklei/go-restful/v3/examples/openapi
    github.com/emicklei/go-restful/v3/examples/user-resource
}

Name:           go-github-emicklei-go-restful-v3
Version:        3.12.2
Release:        %autorelease
Summary:        Package for building REST-style web services in Go
License:        MIT
URL:            https://github.com/emicklei/go-restful
#!RemoteAsset:  sha256:08f387a0aa862ed8698811189d6da92e28b894cc5a7ca45a3ae371d9f339e5a8
Source0:        https://github.com/emicklei/go-restful/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go vet rejects upstream log.Printf with a non-constant format string in
# route_builder.go; keep tests enabled but disable vet. - HNO3Miracle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/emicklei/go-restful/v3) = %{version}

%description
This package provides a framework for building REST-style web services
in Go.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
