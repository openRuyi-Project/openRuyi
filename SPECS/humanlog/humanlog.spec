# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           humanlog
%define go_import_path  github.com/aybabtme/humanlog

Name:           humanlog
Version:        0.4.1
Release:        %autorelease
Summary:        Human-friendly viewer for structured log streams
License:        Apache-2.0
URL:            https://github.com/aybabtme/humanlog
#!RemoteAsset:  sha256:12018abc42c3f62bcf9f4739ec1e6e0016ff993a4566e531d428d866253b2f8e
Source0:        https://github.com/aybabtme/humanlog/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aybabtme/rgbterm)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/go-logfmt/logfmt)
BuildRequires:  go(github.com/kr/logfmt)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/urfave/cli)

%description
humanlog reads structured log streams in JSON or logfmt format from standard
input and renders them as human-friendly, colorized output.

%package     -n go-github-aybabtme-humanlog
Summary:        Human-friendly structured log handling library for Go
BuildArch:      noarch
Provides:       go(github.com/aybabtme/humanlog) = %{version}
Requires:       go(github.com/aybabtme/rgbterm)
Requires:       go(github.com/fatih/color)
Requires:       go(github.com/go-logfmt/logfmt)
Requires:       go(github.com/kr/logfmt)
Requires:       go(github.com/mattn/go-colorable)
Requires:       go(github.com/urfave/cli)

%description -n go-github-aybabtme-humanlog
This package contains the reusable Go source for humanlog, including its
structured log parsers and rendering helpers.

%build
%{go_common}
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
%__go build %{go_build_flags_default} -ldflags "-X main.version=%{version}" \
    -o %{_builddir}/humanlog ./cmd/humanlog

%install
install -D -m 0755 %{_builddir}/humanlog %{buildroot}%{_bindir}/humanlog
%buildsystem_golangmodules_install

%check
%{go_common}
cd %{_builddir}/go/src/%{go_import_path}
%__go test %{shrink:%{go_test_flags_default}} ./...

%files
%doc README*
%license LICENSE*
%{_bindir}/humanlog

%files -n go-github-aybabtme-humanlog
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
