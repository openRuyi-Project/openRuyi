# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           run
%define go_import_path  github.com/oklog/run

Name:           go-github-oklog-run
Version:        1.2.0
Release:        %autorelease
Summary:        A universal mechanism to manage goroutine lifecycles
License:        Apache-2.0
URL:            https://github.com/oklog/run
#!RemoteAsset:  sha256:a27d16ea647cef098c45404806ef087a84f18adce6ea637f81839009280068bc
Source0:        https://github.com/oklog/run/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/oklog/run) = %{version}

%description
run.Group coordinates goroutine lifecycles by running multiple actors,
interrupting the rest when one exits, and waiting for all actors to return.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
