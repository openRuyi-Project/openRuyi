# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           locafero
%define go_import_path  github.com/sagikazarmark/locafero

Name:           go-github-sagikazarmark-locafero
Version:        0.12.0
Release:        %autorelease
Summary:        Finder library for Afero
License:        MIT
URL:            https://github.com/sagikazarmark/locafero
#!RemoteAsset
Source0:        https://github.com/sagikazarmark/locafero/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/spf13/afero)

Provides:       go(github.com/sagikazarmark/locafero) = %{version}

Requires:       go(github.com/spf13/afero)

%description
Finder library for Afero (https://github.com/spf13/afero) ported
from go-finder (https://github.com/sagikazarmark/go-finder).

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
