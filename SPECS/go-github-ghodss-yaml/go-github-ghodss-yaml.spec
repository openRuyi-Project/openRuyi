# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           yaml
%define go_import_path  github.com/ghodss/yaml

Name:           go-github-ghodss-yaml
Version:        1.0.0
Release:        %autorelease
Summary:        Go library for yaml
License:        BSD-3-Clause OR MIT
URL:            https://github.com/ghodss/yaml
VCS:            git:https://github.com/ghodss/yaml.git
#!RemoteAsset:  sha256:8a76b47cd171944612aae1cfa08bbb971b63fec16794c839252808392097de44
Source0:        https://github.com/ghodss/yaml/archive/v1.0.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n yaml-1.0.0

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(github.com/ghodss/yaml) = %{version}

Requires:       go(gopkg.in/yaml.v2)

%description
This package provides the github.com/ghodss/yaml Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
