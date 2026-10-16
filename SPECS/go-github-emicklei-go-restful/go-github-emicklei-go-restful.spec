# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-restful
%define go_import_path  github.com/emicklei/go-restful

Name:           go-github-emicklei-go-restful
Version:        2.9.5
Release:        %autorelease
Summary:        RESTful web services for Go
License:        MIT
URL:            https://github.com/emicklei/go-restful
#!RemoteAsset:  sha256:7781be0cfcc41280191ef87194d9005730fd1971625c5f205dc3f181ac988547
Source0:        https://github.com/emicklei/go-restful/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Legacy test code fails current go vet checks.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/json-iterator/go)

Provides:       go(github.com/emicklei/go-restful) = %{version}

Requires:       go(github.com/json-iterator/go)

%description
RESTful web services for Go.

%prep -a
# Standalone examples require unrelated web frameworks and App Engine services.
rm -rf examples

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
