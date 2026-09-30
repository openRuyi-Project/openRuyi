# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           yaml
%define go_import_path  github.com/ghodss/yaml

Name:           go-github-ghodss-yaml
Version:        1.0.0
Release:        %autorelease
Summary:        YAML marshaling with JSON struct tags for Go
License:        BSD-3-Clause OR MIT
URL:            https://github.com/ghodss/yaml
#!RemoteAsset:  sha256:8a76b47cd171944612aae1cfa08bbb971b63fec16794c839252808392097de44
Source0:        https://github.com/ghodss/yaml/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(github.com/ghodss/yaml) = %{version}

Requires:       go(gopkg.in/yaml.v2)

%description
This library converts YAML to and from JSON and uses Go JSON struct
tags when marshaling YAML data.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
