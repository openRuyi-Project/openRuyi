# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gojq
%define go_import_path  github.com/itchyny/gojq

Name:           gojq
Version:        0.12.15
Release:        %autorelease
Summary:        Pure Go implementation of jq
License:        MIT
URL:            https://github.com/itchyny/gojq
#!RemoteAsset:  sha256:8b450ea96d7d2bc54a92ea9005337955c3e6cdb9a2a0779dc132393d771ea425
Source0:        https://github.com/itchyny/gojq/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/itchyny/timefmt-go)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(gopkg.in/yaml.v3)

%description
gojq is a pure Go implementation of jq that provides JSON query and
transformation functionality as both a command and a reusable library.

%package     -n go-github-itchyny-gojq
Summary:        jq-compatible query library for Go
BuildArch:      noarch
Provides:       go(github.com/itchyny/gojq) = %{version}
Requires:       go(github.com/itchyny/timefmt-go)
Requires:       go(github.com/mattn/go-isatty)
Requires:       go(github.com/mattn/go-runewidth)
Requires:       go(gopkg.in/yaml.v3)

%description -n go-github-itchyny-gojq
This package contains the reusable gojq parser, compiler, iterator and CLI
support source for Go applications.

%build
%{go_common}
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
%__go build %{go_build_flags_default} \
    -ldflags "-X github.com/itchyny/gojq/cli.revision=%{version}" \
    -o %{_builddir}/gojq ./cmd/gojq

%install
install -D -m 0755 %{_builddir}/gojq %{buildroot}%{_bindir}/gojq
%buildsystem_golangmodules_install

%check
%{go_common}
cd %{_builddir}/go/src/%{go_import_path}
# Distro Go encoding/json reports "unexpected end of JSON input" instead of
# the "unexpected EOF" string frozen in gojq 0.12.15 CLI golden output.
%__go test %{shrink:%{go_test_flags_default}} \
    -skip 'TestCliRun/stream_option_with_unterminated_input' \
    ./...

%files
%doc README*
%license LICENSE*
%{_bindir}/gojq

%files -n go-github-itchyny-gojq
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
