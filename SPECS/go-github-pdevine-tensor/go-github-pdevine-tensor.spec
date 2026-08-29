# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tensor
%define go_import_path  github.com/pdevine/tensor
# Upstream does not provide git tags, use commit ID instead - 251
%define commit_id f88f4562727c20425d4b6cad576a4401aa4caa63

Name:           go-github-pdevine-tensor
Version:        0+git20250402.f88f456
Release:        %autorelease
Summary:        package tensor provides efficient and generic n-dimensional arrays in Go that are useful for machine learning and deep learning purposes
License:        Apache-2.0
URL:            https://github.com/pdevine/tensor
#!RemoteAsset:  sha256:284d2f3cfb403bac5218d0142f39de8f92d5af6a820a41622d59a18190d8fd5f
Source0:        https://github.com/pdevine/tensor/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Why the fork don't change the import path? - 251
Patch0:         2000-fix-import-path.patch
# https://github.com/pdevine/tensor/commit/7e32ce7d16dd78f468161089e66b0be6128df67b
Patch1:         0001-fix-test-and-go-deps.patch

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/apache/arrow/go/arrow)
BuildRequires:  go(github.com/chewxy/hm)
BuildRequires:  go(github.com/chewxy/math32)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/flatbuffers)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go4.org/unsafe/assume-no-moving-gc)
BuildRequires:  go(gonum.org/v1/gonum)
BuildRequires:  go(gorgonia.org/vecf32)
BuildRequires:  go(gorgonia.org/vecf64)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3

Provides:       go(github.com/pdevine/tensor) = %{version}

Requires:       go(github.com/apache/arrow/go/arrow)
Requires:       go(github.com/chewxy/hm)
Requires:       go(github.com/chewxy/math32)
Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/google/flatbuffers)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/stretchr/testify)
Requires:       go(go4.org/unsafe/assume-no-moving-gc)
Requires:       go(gonum.org/v1/gonum)
Requires:       go(gorgonia.org/vecf32)
Requires:       go(gorgonia.org/vecf64)

%description
Package tensor is a package that provides efficient, generic (by some
definitions of generic) n-dimensional arrays in Go. Also in this package
are functions and methods that are used commonly in arithmetic,
comparison and linear algebra operations.

The main purpose of this package is to support the operations required
by Gorgonia (https://gorgonia.org/gorgonia).

%check -p
export PYTHON_COMMAND=python3

%files
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
