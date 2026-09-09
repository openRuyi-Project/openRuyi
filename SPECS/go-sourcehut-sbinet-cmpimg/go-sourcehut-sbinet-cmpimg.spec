# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cmpimg
%define go_import_path  git.sr.ht/~sbinet/cmpimg

Name:           go-sourcehut-sbinet-cmpimg
Version:        0.1.0
Release:        %autorelease
Summary:        simple package to compare images
License:        BSD-3-Clause
URL:            https://git.sr.ht/~sbinet/cmpimg
#!RemoteAsset:  sha256:fb13ae7a19cde0a2f4a85e1691db457cbb1d568915ed93e2349d5dd2efad834c
Source0:        https://git.sr.ht/~sbinet/cmpimg/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Avoid relying on exact PNG encoding output changed by Go 1.27.
Patch2000:      2000-Fix-TestDiff-for-Go-1.27-PNG-encoding-changes.patch

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/image)
BuildRequires:  go(rsc.io/pdf)

Provides:       go(git.sr.ht/~sbinet/cmpimg) = %{version}

Requires:       go(golang.org/x/image)
Requires:       go(rsc.io/pdf)

%description
cmpimg is a simple package (extracted from Gonum/plot) to
compare images (PNG, JPEG, PDF, ...)

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
