# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ghw
%define go_import_path  github.com/jaypipes/ghw

Name:           go-github-jaypipes-ghw
Version:        0.11.0
Release:        %autorelease
Summary:        Go library for ghw
License:        Apache-2.0
URL:            https://github.com/jaypipes/ghw
VCS:            git:https://github.com/jaypipes/ghw.git
#!RemoteAsset:  sha256:c53da6d7e087d097ade828a066821bc572f95d60247aaca7b77c521c1a347a16
Source0:        https://github.com/jaypipes/ghw/archive/v0.11.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n ghw-0.11.0
BuildOption(check):  -run '^$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/ghodss/yaml)
BuildRequires:  go(github.com/jaypipes/pcidb)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/spf13/cobra)

Provides:       go(github.com/jaypipes/ghw) = %{version}

Requires:       go(github.com/ghodss/yaml)
Requires:       go(github.com/jaypipes/pcidb)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/spf13/cobra)

%description
This package provides the github.com/jaypipes/ghw Go module source.

%files
%doc README.md
%license COPYING
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
