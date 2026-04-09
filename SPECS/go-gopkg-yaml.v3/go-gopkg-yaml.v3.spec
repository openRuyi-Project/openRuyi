# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           yaml.v3
%define go_import_path  go.yaml.in/yaml/v3

Name:           go-gopkg-yaml.v3
Version:        3.0.4
Release:        %autorelease
Summary:        YAML support for the Go language.
License:        MIT
URL:            https://github.com/yaml/go-yaml
#!RemoteAsset
Source0:        https://github.com/yaml/go-yaml/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(gopkg.in/check.v1)

Provides:       go(gopkg.in/yaml.v3) = %{version}
# Somebody may use this, for example minio
Provides:       go(go.yaml.in/yaml/v3) = %{version}

%description
The yaml package enables Go programs to comfortably encode and decode
YAML values. It was developed within Canonical
(https://www.canonical.com) as part of the juju
(https://juju.ubuntu.com) project, and is based on a pure Go port of the
well-known libyaml (http://pyyaml.org/wiki/LibYAML) C library to parse
and generate YAML data quickly and reliably.

%install -a
# We need to have this linked properly for compatibility
install -d -m 0755 %{buildroot}%{go_sys_gopath}/gopkg.in
ln -s ../%{go_import_path} %{buildroot}%{go_sys_gopath}/gopkg.in/yaml.v3

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}
%{go_sys_gopath}/gopkg.in/yaml.v3

%changelog
%autochangelog
