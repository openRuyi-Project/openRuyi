# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gomodguard
%define go_import_path  github.com/ryancurrah/gomodguard/v2

Name:           go-github-ryancurrah-gomodguard
Version:        2.1.3
Release:        %autorelease
Summary:        Allow and block list linter for direct Go module dependencies
License:        MIT
URL:            https://github.com/ryancurrah/gomodguard
#!RemoteAsset:  sha256:5e285c5346b1499cce84ccfe84b50afbf13568acaea75ef6b11a6245a59e400e
Source0:        https://github.com/ryancurrah/gomodguard/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
# The unversioned v1 API requires its original complete repository snapshot.
#!RemoteAsset:  sha256:2e89fa6a06c0aaa319079d417b41dca7f25c8f87f27b880250ec152633b52497
Source1:        https://github.com/ryancurrah/gomodguard/archive/v1.4.1.tar.gz#/gomodguard-1.4.1.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/Masterminds/semver/v3)
BuildRequires:  go(github.com/bytedance/sonic)
BuildRequires:  go(github.com/chenzhuoyu/base64x)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/gabriel-vasile/mimetype)
BuildRequires:  go(github.com/gin-contrib/sse)
BuildRequires:  go(github.com/gin-gonic/gin)
BuildRequires:  go(github.com/go-playground/locales)
BuildRequires:  go(github.com/go-playground/universal-translator)
BuildRequires:  go(github.com/go-playground/validator/v10)
BuildRequires:  go(github.com/goccy/go-json)
BuildRequires:  go(github.com/gofrs/uuid)
BuildRequires:  go(github.com/gofrs/uuid/v5)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/klauspost/cpuid/v2)
BuildRequires:  go(github.com/leodido/go-urn)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/mitchellh/go-homedir)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/pelletier/go-toml/v2)
BuildRequires:  go(github.com/phayes/checkstyle)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/twitchyliquid64/golang-asm)
BuildRequires:  go(github.com/ugorji/go/codec)
BuildRequires:  go(github.com/uudashr/go-module)
BuildRequires:  go(go.yaml.in/yaml/v4)
BuildRequires:  go(golang.org/x/arch)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(gotest.tools/v3)

Provides:       go(github.com/ryancurrah/gomodguard) = %{version}
Provides:       go(github.com/ryancurrah/gomodguard/cmd/gomodguard/v2) = %{version}
Provides:       go(github.com/ryancurrah/gomodguard/cmd/gomodguard/v2/internal/cli) = %{version}
Provides:       go(github.com/ryancurrah/gomodguard/internal/cli) = %{version}
Provides:       go(github.com/ryancurrah/gomodguard/internal/filesearch) = %{version}
Provides:       go(github.com/ryancurrah/gomodguard/v2) = %{version}

Requires:       go(github.com/Masterminds/semver/v3)
Requires:       go(github.com/mitchellh/go-homedir)
Requires:       go(github.com/phayes/checkstyle)
Requires:       go(go.yaml.in/yaml/v4)
Requires:       go(golang.org/x/mod)
Requires:       go(gopkg.in/yaml.v3)

%description
Allow and block list linter for direct Go module dependencies.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n gomodguard-%{version}
tar -xf %{SOURCE1} -C ..
cp -p ../gomodguard-1.4.1/LICENSE LICENSE.v1

%install -a
# Nested modules use their declared import paths; keep repository fixtures intact.
install -d %{buildroot}%{go_sys_gopath}/github.com/ryancurrah/gomodguard/cmd/gomodguard/v2
cp -a cmd/gomodguard/. %{buildroot}%{go_sys_gopath}/github.com/ryancurrah/gomodguard/cmd/gomodguard/v2/
install -d %{buildroot}%{go_sys_gopath}/github.com/ryancurrah/gomodguard
cp -a ../gomodguard-1.4.1/. %{buildroot}%{go_sys_gopath}/github.com/ryancurrah/gomodguard/

%check
# Stage all modules at their declared paths before testing every package.
%{go_common}
mkdir -p %{_builddir}/go/src/github.com/ryancurrah/gomodguard/cmd/gomodguard/v2
cp -a cmd/gomodguard/. %{_builddir}/go/src/github.com/ryancurrah/gomodguard/cmd/gomodguard/v2/
mkdir -p %{_builddir}/go/src/github.com/ryancurrah/gomodguard/v2
cp -a ./. %{_builddir}/go/src/github.com/ryancurrah/gomodguard/v2/
mkdir -p %{_builddir}/go/src/github.com/ryancurrah/gomodguard
cp -a ../gomodguard-1.4.1/. %{_builddir}/go/src/github.com/ryancurrah/gomodguard/
# Remove staging aliases whose physical paths violate nested internal imports.
rm -rf %{_builddir}/go/src/github.com/ryancurrah/gomodguard/v2/cmd/gomodguard
# The package list omits modules that only declare tool dependencies.
(
    cd %{_builddir}/go/src/github.com/ryancurrah/gomodguard
    packages=$(go list -e -f '{{if or .GoFiles .CgoFiles .TestGoFiles .XTestGoFiles}}{{.ImportPath}}{{end}}' ./...)
    if [ -n "$packages" ]; then
        go test -v $packages
    fi
)

%files
%doc README.md
%license LICENSE LICENSE.v1
%{go_sys_gopath}/github.com/ryancurrah/gomodguard

%changelog
%autochangelog
