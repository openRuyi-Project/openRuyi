# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           multierr
%define go_import_path  go.uber.org/multierr

Name:           go-uber-multierr
Version:        1.11.0
Release:        %autorelease
Summary:        Combine one or more Go errors together
License:        MIT
URL:            https://github.com/uber-go/multierr
#!RemoteAsset
Source0:        https://github.com/uber-go/multierr/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(go.uber.org/multierr) = %{version}

Requires:       go(github.com/stretchr/testify)

%description
multierr allows combining one or more Go errors together.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
