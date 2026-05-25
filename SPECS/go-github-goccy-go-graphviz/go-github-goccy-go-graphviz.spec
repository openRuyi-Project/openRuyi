# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-graphviz
%define go_import_path  github.com/goccy/go-graphviz

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

BuildOption(prep):  -n go-graphviz-0.2.10
# internal/tools/nori is a nested Go module used to generate sources; it has
# its own module path and is not part of the packaged go-graphviz test set.
%define go_test_exclude_glob %{go_import_path}/internal/tools/nori*

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/bufbuild/protocompile)
BuildRequires:  go(github.com/bufbuild/protocompile/linker)
BuildRequires:  go(github.com/bufbuild/protocompile/protoutil)
BuildRequires:  go(github.com/bufbuild/protocompile/reporter)
BuildRequires:  go(github.com/corona10/goimagehash)
BuildRequires:  go(github.com/disintegration/imaging)
BuildRequires:  go(github.com/flopp/go-findfont)
BuildRequires:  go(github.com/fogleman/gg)
BuildRequires:  go(github.com/golang/freetype)
BuildRequires:  go(github.com/golang/freetype/truetype)
BuildRequires:  go(github.com/jessevdk/go-flags)
BuildRequires:  go(github.com/nfnt/resize)
BuildRequires:  go(github.com/tetratelabs/wazero)
BuildRequires:  go(github.com/tetratelabs/wazero/api)
BuildRequires:  go(github.com/tetratelabs/wazero/imports/wasi_snapshot_preview1)
BuildRequires:  go(golang.org/x/image)
BuildRequires:  go(golang.org/x/image/font)
BuildRequires:  go(golang.org/x/image/font/gofont/goregular)
BuildRequires:  go(golang.org/x/image/font/opentype)
BuildRequires:  go(golang.org/x/image/font/sfnt)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/protobuf/proto)
BuildRequires:  go(google.golang.org/protobuf/reflect/protoreflect)
BuildRequires:  go(google.golang.org/protobuf/runtime/protoimpl)
BuildRequires:  go(google.golang.org/protobuf/types/descriptorpb)
BuildRequires:  go(google.golang.org/protobuf/types/dynamicpb)
BuildRequires:  go(google.golang.org/protobuf/types/pluginpb)

Provides:       go(github.com/goccy/go-graphviz) = %{version}
Provides:       go(github.com/goccy/go-graphviz/cdt) = %{version}
Provides:       go(github.com/goccy/go-graphviz/cgraph) = %{version}
Provides:       go(github.com/goccy/go-graphviz/gvc) = %{version}
Provides:       go(github.com/goccy/go-graphviz/internal/wasm) = %{version}

Requires:       go(github.com/bufbuild/protocompile)
Requires:       go(github.com/bufbuild/protocompile/linker)
Requires:       go(github.com/bufbuild/protocompile/protoutil)
Requires:       go(github.com/bufbuild/protocompile/reporter)
Requires:       go(github.com/disintegration/imaging)
Requires:       go(github.com/flopp/go-findfont)
Requires:       go(github.com/fogleman/gg)
Requires:       go(github.com/golang/freetype)
Requires:       go(github.com/golang/freetype/truetype)
Requires:       go(github.com/jessevdk/go-flags)
Requires:       go(github.com/tetratelabs/wazero)
Requires:       go(github.com/tetratelabs/wazero/api)
Requires:       go(github.com/tetratelabs/wazero/imports/wasi_snapshot_preview1)
Requires:       go(golang.org/x/image)
Requires:       go(golang.org/x/image/font)
Requires:       go(golang.org/x/image/font/gofont/goregular)
Requires:       go(golang.org/x/image/font/opentype)
Requires:       go(golang.org/x/image/font/sfnt)
Requires:       go(golang.org/x/term)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/protobuf/proto)
Requires:       go(google.golang.org/protobuf/reflect/protoreflect)
Requires:       go(google.golang.org/protobuf/runtime/protoimpl)
Requires:       go(google.golang.org/protobuf/types/descriptorpb)
Requires:       go(google.golang.org/protobuf/types/dynamicpb)
Requires:       go(google.golang.org/protobuf/types/pluginpb)


%description
This package provides Go bindings and helpers for working with Graphviz.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
