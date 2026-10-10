# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           koanf
%define go_import_path  github.com/knadh/koanf/v2

Name:           go-github-knadh-koanf-v2
Version:        2.3.6
Release:        %autorelease
Summary:        Lightweight extensible configuration management library for Go
License:        MIT
URL:            https://github.com/knadh/koanf
#!RemoteAsset:  sha256:c78d8736d3e27ab78956426a381c2767acf2fa522abe8e709bf87996008e76ab
Source0:        https://github.com/knadh/koanf/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(filippo.io/age)
BuildRequires:  go(filippo.io/edwards25519)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/azcore)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/azidentity)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/internal)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/security/keyvault/azsecrets)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/security/keyvault/internal)
BuildRequires:  go(github.com/AzureAD/microsoft-authentication-library-for-go)
BuildRequires:  go(github.com/BurntSushi/toml)
BuildRequires:  go(github.com/alecthomas/kong)
BuildRequires:  go(github.com/antithesishq/antithesis-sdk-go)
BuildRequires:  go(github.com/armon/go-metrics)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/config)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/credentials)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/feature/ec2/imds)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/configsources)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/endpoints/v2)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/ini)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/appconfig)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/presigned-url)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/ssm)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/sso)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/ssooidc)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/sts)
BuildRequires:  go(github.com/aws/smithy-go)
BuildRequires:  go(github.com/cenkalti/backoff/v3)
BuildRequires:  go(github.com/cenkalti/backoff/v4)
BuildRequires:  go(github.com/coreos/go-semver)
BuildRequires:  go(github.com/coreos/go-systemd/v22)
BuildRequires:  go(github.com/cpuguy83/go-md2man/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/fatih/structs)
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/go-jose/go-jose/v4)
BuildRequires:  go(github.com/go-viper/mapstructure/v2)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/golang-jwt/jwt/v5)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/go-tpm)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/hashicorp/consul/api)
BuildRequires:  go(github.com/hashicorp/errwrap)
BuildRequires:  go(github.com/hashicorp/go-cleanhttp)
BuildRequires:  go(github.com/hashicorp/go-hclog)
BuildRequires:  go(github.com/hashicorp/go-immutable-radix)
BuildRequires:  go(github.com/hashicorp/go-metrics)
BuildRequires:  go(github.com/hashicorp/go-multierror)
BuildRequires:  go(github.com/hashicorp/go-retryablehttp)
BuildRequires:  go(github.com/hashicorp/go-rootcerts)
BuildRequires:  go(github.com/hashicorp/go-secure-stdlib/parseutil)
BuildRequires:  go(github.com/hashicorp/go-secure-stdlib/strutil)
BuildRequires:  go(github.com/hashicorp/go-sockaddr)
BuildRequires:  go(github.com/hashicorp/golang-lru)
BuildRequires:  go(github.com/hashicorp/hcl)
BuildRequires:  go(github.com/hashicorp/serf)
BuildRequires:  go(github.com/hashicorp/vault/api)
BuildRequires:  go(github.com/hjson/hjson-go/v4)
BuildRequires:  go(github.com/huml-lang/go-huml)
BuildRequires:  go(github.com/jmespath/go-jmespath)
BuildRequires:  go(github.com/joho/godotenv)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/kylelemons/godebug)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/minio/highwayhash)
BuildRequires:  go(github.com/mitchellh/copystructure)
BuildRequires:  go(github.com/mitchellh/go-homedir)
BuildRequires:  go(github.com/mitchellh/mapstructure)
BuildRequires:  go(github.com/mitchellh/reflectwalk)
BuildRequires:  go(github.com/nats-io/jwt/v2)
BuildRequires:  go(github.com/nats-io/nats-server/v2)
BuildRequires:  go(github.com/nats-io/nats.go)
BuildRequires:  go(github.com/nats-io/nkeys)
BuildRequires:  go(github.com/nats-io/nuid)
BuildRequires:  go(github.com/npillmayer/nestext)
BuildRequires:  go(github.com/pelletier/go-toml)
BuildRequires:  go(github.com/pelletier/go-toml/v2)
BuildRequires:  go(github.com/pkg/browser)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/rhnvrm/simples3)
BuildRequires:  go(github.com/russross/blackfriday/v2)
BuildRequires:  go(github.com/ryanuber/go-glob)
BuildRequires:  go(github.com/sblinch/kdl-go)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stretchr/objx)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/thunderbottom/kiln)
BuildRequires:  go(github.com/thunderbottom/kiln/pkg/kiln)
BuildRequires:  go(github.com/urfave/cli/v2)
BuildRequires:  go(github.com/urfave/cli/v3)
BuildRequires:  go(github.com/xrash/smetrics)
BuildRequires:  go(go.etcd.io/etcd/api/v3)
BuildRequires:  go(go.etcd.io/etcd/client/pkg/v3)
BuildRequires:  go(go.etcd.io/etcd/client/v3)
BuildRequires:  go(go.uber.org/atomic)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/square/go-jose.v2)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/knadh/koanf/maps) = %{version}
Provides:       go(github.com/knadh/koanf/parsers/dotenv) = %{version}
Provides:       go(github.com/knadh/koanf/parsers/hcl) = %{version}
Provides:       go(github.com/knadh/koanf/parsers/hjson) = %{version}
Provides:       go(github.com/knadh/koanf/parsers/huml) = %{version}
Provides:       go(github.com/knadh/koanf/parsers/json) = %{version}
Provides:       go(github.com/knadh/koanf/parsers/kdl) = %{version}
Provides:       go(github.com/knadh/koanf/parsers/nestedtext) = %{version}
Provides:       go(github.com/knadh/koanf/parsers/toml) = %{version}
Provides:       go(github.com/knadh/koanf/parsers/toml/v2) = %{version}
Provides:       go(github.com/knadh/koanf/parsers/yaml) = %{version}
Provides:       go(github.com/knadh/koanf/providers/appconfig/v2) = %{version}
Provides:       go(github.com/knadh/koanf/providers/azkeyvault) = %{version}
Provides:       go(github.com/knadh/koanf/providers/basicflag) = %{version}
Provides:       go(github.com/knadh/koanf/providers/cliflagv2) = %{version}
Provides:       go(github.com/knadh/koanf/providers/cliflagv3) = %{version}
Provides:       go(github.com/knadh/koanf/providers/confmap) = %{version}
Provides:       go(github.com/knadh/koanf/providers/consul/v2) = %{version}
Provides:       go(github.com/knadh/koanf/providers/env/v2) = %{version}
Provides:       go(github.com/knadh/koanf/providers/etcd/v2) = %{version}
Provides:       go(github.com/knadh/koanf/providers/file) = %{version}
Provides:       go(github.com/knadh/koanf/providers/fs) = %{version}
Provides:       go(github.com/knadh/koanf/providers/k8smount) = %{version}
Provides:       go(github.com/knadh/koanf/providers/kiln) = %{version}
Provides:       go(github.com/knadh/koanf/providers/nats) = %{version}
Provides:       go(github.com/knadh/koanf/providers/parameterstore/v2) = %{version}
Provides:       go(github.com/knadh/koanf/providers/posflag) = %{version}
Provides:       go(github.com/knadh/koanf/providers/rawbytes) = %{version}
Provides:       go(github.com/knadh/koanf/providers/s3) = %{version}
Provides:       go(github.com/knadh/koanf/providers/structs) = %{version}
Provides:       go(github.com/knadh/koanf/providers/vault/v2) = %{version}
Provides:       go(github.com/knadh/koanf/v2) = %{version}
Provides:       go-github-knadh-koanf-maps = %{version}-%{release}
Provides:       go-github-knadh-koanf-providers-confmap = %{version}-%{release}

Obsoletes:      go-github-knadh-koanf-maps
Obsoletes:      go-github-knadh-koanf-providers-confmap

Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/azidentity)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/security/keyvault/azsecrets)
Requires:       go(github.com/aws/aws-sdk-go-v2)
Requires:       go(github.com/aws/aws-sdk-go-v2/config)
Requires:       go(github.com/aws/aws-sdk-go-v2/credentials)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/appconfig)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/ssm)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/sts)
Requires:       go(github.com/aws/smithy-go)
Requires:       go(github.com/fatih/structs)
Requires:       go(github.com/fsnotify/fsnotify)
Requires:       go(github.com/go-viper/mapstructure/v2)
Requires:       go(github.com/hashicorp/consul/api)
Requires:       go(github.com/hashicorp/hcl)
Requires:       go(github.com/hashicorp/vault/api)
Requires:       go(github.com/hjson/hjson-go/v4)
Requires:       go(github.com/huml-lang/go-huml)
Requires:       go(github.com/joho/godotenv)
Requires:       go(github.com/mitchellh/copystructure)
Requires:       go(github.com/mitchellh/reflectwalk)
Requires:       go(github.com/nats-io/nats.go)
Requires:       go(github.com/npillmayer/nestext)
Requires:       go(github.com/pelletier/go-toml/v2)
Requires:       go(github.com/rhnvrm/simples3)
Requires:       go(github.com/sblinch/kdl-go)
Requires:       go(github.com/spf13/pflag)
Requires:       go(github.com/thunderbottom/kiln)
Requires:       go(github.com/thunderbottom/kiln/pkg/kiln)
Requires:       go(github.com/urfave/cli/v2)
Requires:       go(github.com/urfave/cli/v3)
Requires:       go(go.etcd.io/etcd/client/v3)
Requires:       go(go.yaml.in/yaml/v3)

%description
Koanf is a library for reading configuration from multiple sources and
providing it through a consistent Go API. This package installs every Go
module contained in the upstream repository.

%install
# Read module declarations without invoking Go module resolution; OBS tests
# use GOPATH and must not fetch dependencies while discovering source paths.
while IFS= read -r modfile; do
    moddir="${modfile%/go.mod}"
    modpath=$(awk '$1 == "module" {gsub(/"/, "", $2); print $2; exit}' "${modfile}")
    test -n "${modpath}"
    install -d "%{buildroot}%{go_sys_gopath}/${modpath}"
    if [ "${moddir}" = "." ]; then
        install -p -m 0644 *.go go.mod go.sum \
            "%{buildroot}%{go_sys_gopath}/${modpath}/"
    else
        cp -a "${moddir}"/. "%{buildroot}%{go_sys_gopath}/${modpath}/"
    fi
done < <(find . -name go.mod -not -path './.git/*' | sort)

# The integration tests still import the pre-v2 TOML parser path.
install -d %{buildroot}%{go_sys_gopath}/github.com/knadh/koanf/parsers/toml
cp -a parsers/toml/. \
    %{buildroot}%{go_sys_gopath}/github.com/knadh/koanf/parsers/toml/
cp -a mock %{buildroot}%{go_sys_gopath}/github.com/knadh/koanf/

%check
%go_common
# Test this build's canonical module paths, not older system-installed copies.
install -d %{_builddir}/go/src
cp -a %{buildroot}%{go_sys_gopath}/. %{_builddir}/go/src/
while IFS= read -r modfile; do
    moddir="${modfile%/go.mod}"
    modpath=$(awk '$1 == "module" {gsub(/"/, "", $2); print $2; exit}' "${modfile}")
    test -n "${modpath}"
    go test -v "${modpath}/..."
done < <(find . -name go.mod -not -path './.git/*' | sort)

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/github.com/knadh/koanf

%changelog
%autochangelog
