# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-graphviz
%define go_import_path  github.com/goccy/go-graphviz
# internal/tools/nori is a nested Go module used to generate sources; it has
# its own module path and is not part of the packaged go-graphviz test set.
# - HNO3Miracle
%define go_test_exclude_glob %{go_import_path}/internal/tools/nori*

Name:           go-github-goccy-go-graphviz
Version:        0.2.10
Release:        %autorelease
Summary:        Graphviz library for Go
License:        MIT
URL:            https://github.com/goccy/go-graphviz
#!RemoteAsset:  sha256:34328369f97388963577bccc4dde41429a31d3b4fb0010f54f82984f21235d70
Source0:        https://github.com/goccy/go-graphviz/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/bufbuild/protocompile)
BuildRequires:  go(github.com/corona10/goimagehash)
BuildRequires:  go(github.com/disintegration/imaging)
BuildRequires:  go(github.com/flopp/go-findfont)
BuildRequires:  go(github.com/fogleman/gg)
BuildRequires:  go(github.com/golang/freetype)
BuildRequires:  go(github.com/jessevdk/go-flags)
BuildRequires:  go(github.com/nfnt/resize)
BuildRequires:  go(github.com/tetratelabs/wazero)
BuildRequires:  go(golang.org/x/image)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/goccy/go-graphviz) = %{version}

Requires:       go(github.com/bufbuild/protocompile)
Requires:       go(github.com/disintegration/imaging)
Requires:       go(github.com/flopp/go-findfont)
Requires:       go(github.com/fogleman/gg)
Requires:       go(github.com/golang/freetype)
Requires:       go(github.com/jessevdk/go-flags)
Requires:       go(github.com/tetratelabs/wazero)
Requires:       go(golang.org/x/image)
Requires:       go(golang.org/x/term)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/protobuf)

%description
This package provides Go bindings and helpers for working with Graphviz.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
