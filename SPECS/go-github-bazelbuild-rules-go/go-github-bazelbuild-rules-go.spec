# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           rules_go
%define go_import_path  github.com/bazelbuild/rules_go
# These packages are Bazel actions or integration-test harnesses. They require
# Bazel-selected source files, generated fixtures, runfiles, or Go internal
# packages and therefore cannot be tested as ordinary GOPATH packages.
%define go_test_exclude_glob  %{shrink:
    %{go_import_path}/go/private
    %{go_import_path}/go/tools/builders
    %{go_import_path}/go/tools/bzltestutil/bincov
    %{go_import_path}/go/tools/gopackagesdriver
    %{go_import_path}/tests/*
}
# These nested command modules intentionally rely on dependencies injected by
# Bazel rather than declaring them in their go.mod files.
%define go_test_exclude  %{shrink:
    %{go_import_path}/examples/basic_gazelle
    %{go_import_path}/go/tools/fetch_repo
    %{go_import_path}/go/tools/releaser
}

Name:           go-github-bazelbuild-rules-go
Version:        0.62.0
Release:        %autorelease
Summary:        Bazel rules for building Go code
License:        Apache-2.0
URL:            https://github.com/bazelbuild/rules_go
#!RemoteAsset:  sha256:988a8856e5cf6ce5bcb1e30919fe87e444af0fe09ae26ae125035c9522bda147
Source0:        https://github.com/bazelbuild/rules_go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

BuildRequires:  go(github.com/aymanbagabas/go-udiff)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/golang/mock)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v2)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/go/runfiles) = %{version}
Provides:       go(github.com/bazel-contrib/rules_go/examples/basic_gazelle) = %{version}

Requires:       go(github.com/aymanbagabas/go-udiff)
Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/golang/protobuf)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/tools)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/yaml.v2)

%description
Rules_go provides Bazel rules for building, testing, and managing Go code,
including toolchain, library, binary, test, and protocol buffer integration.

%install -a
# basic_gazelle is a nested module whose declared import path uses the
# bazel-contrib organization, so move it out of the enclosing repository path.
install -d %{buildroot}%{go_sys_gopath}/github.com/bazel-contrib/rules_go/examples
mv %{buildroot}%{go_sys_gopath}/%{go_import_path}/examples/basic_gazelle \
    %{buildroot}%{go_sys_gopath}/github.com/bazel-contrib/rules_go/examples/

%check -p
# Prepare the differently named nested module at its canonical GOPATH before
# the default check copies and tests the enclosing rules_go repository.
%go_common
install -d %{_builddir}/go/src/github.com/bazel-contrib/rules_go/examples
cp -a examples/basic_gazelle \
    %{_builddir}/go/src/github.com/bazel-contrib/rules_go/examples/
# Bazel normally exports these paths for go/tools/bazel tests. Point them at
# the GOPATH tree that the default check creates from the same source archive.
export TEST_SRCDIR=%{_builddir}/go/src
export TEST_WORKSPACE=%{go_import_path}

%check -a
# The default ./... check sees basic_gazelle only at the enclosing repository
# path; test it separately under the import path declared by its go.mod file.
cd %{_builddir}/go/src/github.com/bazel-contrib/rules_go/examples/basic_gazelle
go test -v ./...

%files
%doc README.rst
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}
%{go_sys_gopath}/github.com/bazel-contrib/rules_go

%changelog
%autochangelog
