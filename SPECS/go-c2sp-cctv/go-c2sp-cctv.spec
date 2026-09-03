# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           CCTV
%define go_import_path  c2sp.org/CCTV
%define commit_id       4448f2097b2daa812c91a26141f9f36c2096b9ca

Name:           go-c2sp-cctv
Version:        0+git20260902.4448f20
Release:        %autorelease
Summary:        Community cryptography test vectors
License:        BSD-3-Clause AND (0BSD OR CC0-1.0 OR Unlicense)
URL:            https://github.com/C2SP/CCTV
#!RemoteAsset:  sha256:a947dca9b63d4d9d33c3af1811be89dfd655156e266d1aa339b231c8c9569c97
Source0:        https://github.com/C2SP/CCTV/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Adapt the ed25519 vectors to the current edwards25519 API in openruyi.
Patch0:         2000-ed25519-current-api.patch

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go(filippo.io/edwards25519)
BuildRequires:  go(github.com/evanw/esbuild)
BuildRequires:  go(github.com/hdevalence/ed25519consensus)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go-rpm-macros

Provides:       go(c2sp.org/CCTV/age) = %{version}
Provides:       go(c2sp.org/CCTV/ed25519) = %{version}
Provides:       go(c2sp.org/CCTV/ML-KEM/modulus) = %{version}
Provides:       go(c2sp.org/CCTV/ML-KEM/unluckysample) = %{version}

Requires:       go(filippo.io/edwards25519)
Requires:       go(github.com/evanw/esbuild)
Requires:       go(github.com/hdevalence/ed25519consensus)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sys)

%description
CCTV collects reusable cryptographic test vectors. This package installs all
Go modules contained in the upstream repository.

%install
while IFS= read -r modfile; do
    moddir="${modfile%/go.mod}"
    modpath=$(cd "${moddir}" && GO111MODULE=on GOWORK=off go list -m -f '{{.Path}}')
    install -d "%{buildroot}%{go_sys_gopath}/${modpath}"
    cp -a "${moddir}"/. "%{buildroot}%{go_sys_gopath}/${modpath}/"
done < <(find . -name go.mod -not -path './.git/*' | sort)

%check
%go_common
# Match the GOPATH layout prepared above.
install -d %{_builddir}/go/src
cp -a %{buildroot}%{go_sys_gopath}/. %{_builddir}/go/src/
while IFS= read -r modfile; do
    moddir="${modfile%/go.mod}"
    modpath=$(cd "${moddir}" && GO111MODULE=on GOWORK=off go list -m -f '{{.Path}}')
    # Some modules contain only test vectors and no Go package.
    packages=$(cd "${moddir}" && go list -e -f '{{.ImportPath}}' ./... 2>/dev/null || :)
    if [ -z "${packages}" ]; then
        continue
    fi
    go test -v "${modpath}/..."
done < <(find . -name go.mod -not -path './.git/*' | sort)

%files
%doc README.md
%license age/README.md age/internal/LICENSE ed25519/LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
