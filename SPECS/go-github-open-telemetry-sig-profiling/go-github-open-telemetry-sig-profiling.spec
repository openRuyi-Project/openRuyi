# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sig-profiling
%define go_import_path  github.com/open-telemetry/sig-profiling
# This package invokes a Docker image to regenerate protobuf test fixtures.
%define go_test_exclude %{go_import_path}/otlp-bench/internal/otlpbuild
%define commit_id       2572075a475a2446ed931efa2eba31f40edc3dc6

Name:           go-github-open-telemetry-sig-profiling
Version:        0+git20260819.2572075
Release:        %autorelease
Summary:        OpenTelemetry profiling development tools
License:        Apache-2.0
URL:            https://github.com/open-telemetry/sig-profiling
#!RemoteAsset:  sha256:09f5418dfbe3e68a8f4816bda15e47d8db280baf75b5f34bd3cc871faa074c19
Source0:        https://github.com/open-telemetry/sig-profiling/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules
BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/lmittmann/tint)
BuildRequires:  go(github.com/urfave/cli/v3)
BuildRequires:  go(go.opentelemetry.io/proto)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/lmittmann/tint)
Requires:       go(github.com/urfave/cli/v3)
Requires:       go(go.opentelemetry.io/proto)
Requires:       go(google.golang.org/protobuf)

%description
This package contains the OpenTelemetry Profiling SIG's profile validation
and OTLP benchmarking tools from one repository snapshot.

%check
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
install -d %{_builddir}/go/src/%{go_import_path}
cp -a . %{_builddir}/go/src/%{go_import_path}
pushd %{_builddir}/go/src/%{go_import_path}
while IFS= read -r -d '' go_mod; do
    pushd "$(dirname "${go_mod}")"
    for package in $(go list -e -f '{{.ImportPath}}' ./...); do
        case " %{go_test_exclude} " in
            *" ${package} "*) go test -c -o /dev/null "${package}" ;;
            *) go test -v "${package}" ;;
        esac
    done
    popd
done < <(find . -name go.mod -print0)
popd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
