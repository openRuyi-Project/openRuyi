# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           memory
%define go_import_path  github.com/pbnjay/memory
%define commit_id 7b4eea64cf580186c0eceb10dc94ba3a098af46c

Name:           go-github-pbnjay-memory
Version:        0+git20260607.7b4eea6
Release:        %autorelease
Summary:        A go function to report total system memory
License:        BSD-3-Clause
URL:            https://github.com/pbnjay/memory
#!RemoteAsset:  sha256:ce834a1e491ef8f028b5711fde615218e8d00dafdeca86e1b1bf32e0f8245376
Source0:        https://github.com/pbnjay/memory/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/pbnjay/memory) = %{version}

%description
Package memory provides two methods reporting total physical system
memory accessible to the kernel, and free memory available to the
running application.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
