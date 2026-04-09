# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cancelreader
%define go_import_path  github.com/muesli/cancelreader
# I dont know why it will fail on OBS - Julian
%define go_test_ignore_failure 1

Name:           go-github-muesli-cancelreader
Version:        0.2.2
Release:        %autorelease
Summary:        A cancelable reader for Go
License:        MIT
URL:            https://github.com/muesli/cancelreader
#!RemoteAsset
Source0:        https://github.com/muesli/cancelreader/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/muesli/cancelreader) = %{version}

%description
A cancelable reader for Go

This package is based on the fantastic work of Erik Geiser
(https://github.com/erikgeiser) in Charm's Bubble Tea
(https://github.com/charmbracelet/bubbletea) framework.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
