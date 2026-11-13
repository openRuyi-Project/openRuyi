# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           dst
%define go_import_path  github.com/dave/dst

Name:           go-github-dave-dst
Version:        0.28.0
Release:        %autorelease
Summary:        Decorated Go syntax trees
License:        MIT AND BSD-3-Clause
URL:            https://github.com/dave/dst
#!RemoteAsset:  sha256:bd6332e95f60eb2758e7046d34db934cd02e3e42e84ac68ad06f785b0588a0cb
Source0:        https://github.com/dave/dst/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Load temporary go.mod fixtures without changing tests of GOPATH dependencies.
Patch2000:      2000-tests-load-temporary-module-fixtures-in-module-mode.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/dave/jennifer)
BuildRequires:  go(github.com/sergi/go-diff)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(gopkg.in/src-d/go-billy.v4)

Provides:       go(github.com/dave/dst) = %{version}
Provides:       go(github.com/dave/dst/decorator) = %{version}
Provides:       go(github.com/dave/dst/decorator/resolver) = %{version}
Provides:       go(github.com/dave/dst/decorator/resolver/goast) = %{version}
Provides:       go(github.com/dave/dst/decorator/resolver/gobuild) = %{version}
Provides:       go(github.com/dave/dst/decorator/resolver/gopackages) = %{version}
Provides:       go(github.com/dave/dst/decorator/resolver/gotypes) = %{version}
Provides:       go(github.com/dave/dst/decorator/resolver/guess) = %{version}
Provides:       go(github.com/dave/dst/decorator/resolver/simple) = %{version}
Provides:       go(github.com/dave/dst/dstutil) = %{version}
Provides:       go(github.com/dave/dst/gendst/data) = %{version}

Requires:       go(github.com/dave/jennifer)
Requires:       go(github.com/sergi/go-diff)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/tools)
Requires:       go(gopkg.in/src-d/go-billy.v4)

%description
DST preserves comments and formatting when manipulating Go syntax trees.
It includes decorators, import resolvers, and source restoration helpers.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
