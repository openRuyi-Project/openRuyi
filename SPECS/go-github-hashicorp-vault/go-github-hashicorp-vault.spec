# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           api
%define go_import_path  github.com/hashicorp/vault/api

Name:           go-github-hashicorp-vault
Version:        1.23.0
Release:        %autorelease
Summary:        Go client library for HashiCorp Vault
License:        MPL-2.0
URL:            https://github.com/hashicorp/vault
#!RemoteAsset:  sha256:3c63ed5e2f7459dc1b63ef4746b202ec79244af4e7bac82c892a265f7edc0495
Source0:        https://github.com/hashicorp/vault/archive/refs/tags/api/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Use credential types exported by current cloud.google.com/go/iam.
Patch2000:      2000-use-cloud-iam-credential-types.patch

# The API release archive contains the Vault repository, not an api-only tree.
BuildOption(prep):  -n vault-api-v%{version}

BuildRequires:  go
BuildRequires:  go(cloud.google.com/go/auth)
BuildRequires:  go(cloud.google.com/go/auth/oauth2adapt)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(cloud.google.com/go/iam)
BuildRequires:  go(github.com/aws/aws-sdk-go)
BuildRequires:  go(github.com/cenkalti/backoff/v4)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/go-jose/go-jose/v4)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/go-test/deep)
BuildRequires:  go(github.com/google/s2a-go)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(github.com/hashicorp/errwrap)
BuildRequires:  go(github.com/hashicorp/go-cleanhttp)
BuildRequires:  go(github.com/hashicorp/go-hclog)
BuildRequires:  go(github.com/hashicorp/go-multierror)
BuildRequires:  go(github.com/hashicorp/go-retryablehttp)
BuildRequires:  go(github.com/hashicorp/go-rootcerts)
BuildRequires:  go(github.com/hashicorp/go-secure-stdlib/awsutil)
BuildRequires:  go(github.com/hashicorp/go-secure-stdlib/parseutil)
BuildRequires:  go(github.com/hashicorp/go-secure-stdlib/strutil)
BuildRequires:  go(github.com/hashicorp/go-sockaddr)
BuildRequires:  go(github.com/hashicorp/go-uuid)
BuildRequires:  go(github.com/hashicorp/hcl)
BuildRequires:  go(github.com/jmespath/go-jmespath)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/mitchellh/go-homedir)
BuildRequires:  go(github.com/mitchellh/mapstructure)
BuildRequires:  go(github.com/natefinch/atomic)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/ryanuber/go-glob)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/metric)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(google.golang.org/api)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/hashicorp/vault/api) = %{version}
Provides:       go(github.com/hashicorp/vault/api/auth/approle) = %{version}
Provides:       go(github.com/hashicorp/vault/api/auth/aws) = %{version}
Provides:       go(github.com/hashicorp/vault/api/auth/azure) = %{version}
Provides:       go(github.com/hashicorp/vault/api/auth/cert) = %{version}
Provides:       go(github.com/hashicorp/vault/api/auth/gcp) = %{version}
Provides:       go(github.com/hashicorp/vault/api/auth/kubernetes) = %{version}
Provides:       go(github.com/hashicorp/vault/api/auth/ldap) = %{version}
Provides:       go(github.com/hashicorp/vault/api/auth/userpass) = %{version}
Provides:       go(github.com/hashicorp/vault/api/cliconfig) = %{version}
Provides:       go(github.com/hashicorp/vault/api/tokenhelper) = %{version}

Requires:       go(cloud.google.com/go/compute/metadata)
Requires:       go(cloud.google.com/go/iam)
Requires:       go(github.com/aws/aws-sdk-go)
Requires:       go(github.com/cenkalti/backoff/v4)
Requires:       go(github.com/go-jose/go-jose/v4)
Requires:       go(github.com/hashicorp/errwrap)
Requires:       go(github.com/hashicorp/go-cleanhttp)
Requires:       go(github.com/hashicorp/go-hclog)
Requires:       go(github.com/hashicorp/go-multierror)
Requires:       go(github.com/hashicorp/go-retryablehttp)
Requires:       go(github.com/hashicorp/go-rootcerts)
Requires:       go(github.com/hashicorp/go-secure-stdlib/awsutil)
Requires:       go(github.com/hashicorp/go-secure-stdlib/parseutil)
Requires:       go(github.com/hashicorp/go-secure-stdlib/strutil)
Requires:       go(github.com/hashicorp/go-uuid)
Requires:       go(github.com/hashicorp/hcl)
Requires:       go(github.com/mitchellh/go-homedir)
Requires:       go(github.com/mitchellh/mapstructure)
Requires:       go(github.com/natefinch/atomic)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/time)
Requires:       go(google.golang.org/genproto)

%description
This package provides the Go client API for interacting with HashiCorp Vault.

# Keep only the API module and move its contents to the module root. Without
# this normalization, the archive would install it below .../vault/api/api.
%prep -a
find . -mindepth 1 -maxdepth 1 ! -name api -exec rm -rf {} +
shopt -s dotglob
mv api/* .
rmdir api

%install
%buildsystem_golangmodules_install

%check
%go_common
# Test every declared nested module from its canonical GOPATH location. The
# standard macro only discovers packages in the current module, so testing the
# root alone would silently omit sibling modules.
install -d "%{_builddir}/go/src"
cp -a "%{buildroot}%{go_sys_gopath}/." "%{_builddir}/go/src/"
_module_files=$(find . -name go.mod -not -path './.git/*' -not -path '*/testdata/*' | sort)
_test_module() {
    _go_packages=$(go list -e -f '{{.ImportPath}}' ./...)
    _go_tests=
    set -f
    for _package in ${_go_packages}; do
        _skip=0
        for _exclude in %{?go_test_exclude}; do
            [ "${_package}" = "${_exclude}" ] && _skip=1
        done
        for _exclude in %{?go_test_exclude_glob}; do
            case "${_package}" in ${_exclude}) _skip=1 ;; esac
        done
        [ "${_skip}" -eq 0 ] && _go_tests="${_go_tests} ${_package}"
    done
    set +f
    [ -z "${_go_tests}" ] || go test %{go_test_flags_default} ${_go_tests}
}
while read -r _modfile; do
    _source=${_modfile%/go.mod}
    _import=$(awk '$1 == "module" {gsub(/"/, "", $2); print $2; exit}' "${_modfile}")
    case "${_import}" in
        github.com/hashicorp/vault/api|github.com/hashicorp/vault/api/*) ;;
        *) continue ;;
    esac
    pushd "%{_builddir}/go/src/${_import}"
    _test_module
    popd
done <<EOF
${_module_files}
EOF
%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
