# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           regclient
%define go_import_path  github.com/regclient/regclient

Name:           go-github-regclient-regclient
Version:        0.4.8
Release:        %autorelease
Summary:        Is used to access OCI registries
License:        Apache-2.0
URL:            https://github.com/regclient/regclient
VCS:            git:https://github.com/regclient/regclient.git
#!RemoteAsset:  sha256:9c06fd37df493b5b8f42f0a96174beebaf00012a8826c49c17081687cd0e12f4
Source0:        https://github.com/regclient/regclient/archive/v0.4.8.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n regclient-0.4.8
BuildOption(check):  -skip '^TestDataJSON$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/docker/libtrust)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/opencontainers/go-digest)
BuildRequires:  go(github.com/robfig/cron/v3)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/yuin/gopher-lua)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(github.com/regclient/regclient) = %{version}

Requires:       go(github.com/docker/libtrust)
Requires:       go(github.com/opencontainers/go-digest)
Requires:       go(github.com/robfig/cron/v3)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(github.com/spf13/cobra)
Requires:       go(github.com/yuin/gopher-lua)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/term)
Requires:       go(gopkg.in/yaml.v2)

%description
This package provides the github.com/regclient/regclient Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
