# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           yaml.v2
%define go_import_path  gopkg.in/yaml.v2

Name:           go-gopkg-yaml.v2
Version:        2.4.0
Release:        %autorelease
Summary:        YAML support for the Go language.
License:        Apache-2.0
URL:            https://github.com/go-yaml/yaml
#!RemoteAsset
Source0:        https://github.com/go-yaml/yaml/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(gopkg.in/check.v1)

Provides:       go(gopkg.in/yaml.v2) = %{version}
# Somebody may use this, for example github.com/prometheus/common
Provides:       go(go.yaml.in/yaml/v2) = %{version}

%description
The yaml package enables Go programs to comfortably encode and decode
YAML values. It was developed within Canonical
(https://www.canonical.com) as part of the juju
(https://juju.ubuntu.com) project, and is based on a pure Go port of the
well-known libyaml (http://pyyaml.org/wiki/LibYAML) C library to parse
and generate YAML data quickly and reliably.

%install -a
# Compatibility import path go.yaml.in/yaml.v2
install -d -m 0755 %{buildroot}%{go_sys_gopath}
install -d -m 0755 %{buildroot}%{go_sys_gopath}/go.yaml.in/yaml
ln -s ../../%{go_import_path} %{buildroot}%{go_sys_gopath}/go.yaml.in/yaml/v2

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}
%{go_sys_gopath}/go.yaml.in/yaml/v2

%changelog
%autochangelog
