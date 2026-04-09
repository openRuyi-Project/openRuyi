# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gg
%define go_import_path  git.sr.ht/~sbinet/gg
# only riscv64 fails tho - 251
%define go_test_exclude git.sr.ht/~sbinet/gg/examples

Name:           go-sourcehut-sbinet-gg
Version:        0.7.0
Release:        %autorelease
Summary:        gg is a library for rendering 2D graphics in pure Go.
License:        MIT
URL:            https://git.sr.ht/~sbinet/gg
#!RemoteAsset
Source0:        https://git.sr.ht/~sbinet/gg/archive/v%{version}.tar.gz#/%{_name}-v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-v%{version}
BuildOption(check):  -short

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(codeberg.org/go-fonts/anton)
BuildRequires:  go(codeberg.org/go-fonts/liberation)
BuildRequires:  go(codeberg.org/go-fonts/xolonium)
BuildRequires:  go(git.sr.ht/~sbinet/cmpimg)
BuildRequires:  go(github.com/golang/freetype)
BuildRequires:  go(golang.org/x/image)

Provides:       go(git.sr.ht/~sbinet/gg) = %{version}

Requires:       go(codeberg.org/go-fonts/anton)
Requires:       go(codeberg.org/go-fonts/liberation)
Requires:       go(codeberg.org/go-fonts/xolonium)
Requires:       go(git.sr.ht/~sbinet/cmpimg)
Requires:       go(github.com/golang/freetype)
Requires:       go(golang.org/x/image)

%description
gg is a library for rendering 2D graphics in pure Go.

git.sr.ht/~sbinet/gg is a fork of fogleman/gg which doesn't
seem to be maintained (as of January 2022).

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
