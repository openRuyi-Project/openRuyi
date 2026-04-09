# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-syslog
%define go_import_path  github.com/hashicorp/go-syslog

Name:           go-github-hashicorp-go-syslog
Version:        1.0.0
Release:        %autorelease
Summary:        Golang syslog wrapper, cross-compile friendly
License:        MIT
URL:            https://github.com/hashicorp/go-syslog
#!RemoteAsset
Source0:        https://github.com/hashicorp/go-syslog/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/hashicorp/go-syslog) = %{version}

%description
This repository provides a very simple gsyslog package. The point of
this package is to allow safe importing of syslog without introducing
cross-compilation issues. The stdlib log/syslog cannot be imported on
Windows systems, and without conditional compilation this adds
complications.

Instead, gsyslog provides a very simple wrapper around log/syslog but
returns a runtime error if attempting to initialize on a non Linux or
OSX system.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
