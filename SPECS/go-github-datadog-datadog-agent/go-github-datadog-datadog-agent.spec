# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           datadog-agent
%define go_import_path  github.com/DataDog/datadog-agent
%define commit          7c02565fb890b34e37ee3aadb9efa6d87fa8aa69

Name:           go-github-datadog-datadog-agent
Version:        7.78.4+git20260817.7c02565
Release:        %autorelease
Summary:        Datadog Agent Go source modules
License:        Apache-2.0
URL:            https://github.com/DataDog/datadog-agent
#!RemoteAsset:  sha256:b2a6db773ac91a9d7a9ff0f3d1034bf44a1c20065a0615295e3706a3488f6556
Source0:        https://github.com/DataDog/datadog-agent/archive/%{commit}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit}

BuildRequires:  go
BuildRequires:  go(4d63.com/gocheckcompilerdirectives)
BuildRequires:  go(4d63.com/gochecknoglobals)
BuildRequires:  go(cel.dev/expr)
BuildRequires:  go(charm.land/lipgloss/v2)
BuildRequires:  go(cloud.google.com/go)
BuildRequires:  go(cloud.google.com/go/auth)
BuildRequires:  go(cloud.google.com/go/auth/oauth2adapt)
BuildRequires:  go(cloud.google.com/go/cloudsqlconn)
BuildRequires:  go(cloud.google.com/go/compute)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(cloud.google.com/go/iam)
BuildRequires:  go(cloud.google.com/go/kms)
BuildRequires:  go(cloud.google.com/go/longrunning)
BuildRequires:  go(cloud.google.com/go/monitoring)
BuildRequires:  go(code.cloudfoundry.org/bbs)
BuildRequires:  go(code.cloudfoundry.org/cfhttp/v2)
BuildRequires:  go(code.cloudfoundry.org/clock)
BuildRequires:  go(code.cloudfoundry.org/consuladapter)
BuildRequires:  go(code.cloudfoundry.org/diego-logging-client)
BuildRequires:  go(code.cloudfoundry.org/executor)
BuildRequires:  go(code.cloudfoundry.org/garden)
BuildRequires:  go(code.cloudfoundry.org/go-diodes)
BuildRequires:  go(code.cloudfoundry.org/go-loggregator)
BuildRequires:  go(code.cloudfoundry.org/lager)
BuildRequires:  go(code.cloudfoundry.org/locket)
BuildRequires:  go(code.cloudfoundry.org/rep)
BuildRequires:  go(code.cloudfoundry.org/rfc5424)
BuildRequires:  go(code.cloudfoundry.org/tlsconfig)
BuildRequires:  go(codeberg.org/chavacava/garif)
BuildRequires:  go(codeberg.org/polyfloyd/go-errorlint)
BuildRequires:  go(cyphar.com/go-pathrs)
BuildRequires:  go(dario.cat/mergo)
BuildRequires:  go(dev.gaijin.team/go/exhaustruct/v4)
BuildRequires:  go(dev.gaijin.team/go/golib)
BuildRequires:  go(filippo.io/edwards25519)
BuildRequires:  go(github.com/4meepo/tagalign)
BuildRequires:  go(github.com/Abirdcfly/dupword)
BuildRequires:  go(github.com/AdaLogics/go-fuzz-headers)
BuildRequires:  go(github.com/AdamKorcz/go-118-fuzz-build)
BuildRequires:  go(github.com/AdminBenni/iota-mixing)
BuildRequires:  go(github.com/AlekSi/pointer)
BuildRequires:  go(github.com/AlwxSin/noinlineerr)
BuildRequires:  go(github.com/Antonboom/errname)
BuildRequires:  go(github.com/Antonboom/nilnil)
BuildRequires:  go(github.com/Antonboom/testifylint)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/azcore)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/azidentity)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/internal)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/keyvault/azkeys)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/keyvault/internal)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/compute/armcompute/v5)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/network/armnetwork/v4)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/resources/armresources)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/security/keyvault/azsecrets)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/security/keyvault/internal)
BuildRequires:  go(github.com/Azure/go-ansiterm)
BuildRequires:  go(github.com/Azure/go-autorest)
BuildRequires:  go(github.com/Azure/go-autorest/autorest)
BuildRequires:  go(github.com/Azure/go-autorest/autorest/adal)
BuildRequires:  go(github.com/Azure/go-autorest/autorest/azure/auth)
BuildRequires:  go(github.com/Azure/go-autorest/autorest/azure/cli)
BuildRequires:  go(github.com/Azure/go-autorest/autorest/date)
BuildRequires:  go(github.com/Azure/go-autorest/autorest/to)
BuildRequires:  go(github.com/Azure/go-autorest/autorest/validation)
BuildRequires:  go(github.com/Azure/go-autorest/logger)
BuildRequires:  go(github.com/Azure/go-autorest/tracing)
BuildRequires:  go(github.com/AzureAD/microsoft-authentication-library-for-go)
BuildRequires:  go(github.com/BurntSushi/toml)
BuildRequires:  go(github.com/ClickHouse/clickhouse-go-linter)
BuildRequires:  go(github.com/Code-Hex/go-generics-cache)
BuildRequires:  go(github.com/CycloneDX/cyclonedx-go)
BuildRequires:  go(github.com/DATA-DOG/go-sqlmock)
BuildRequires:  go(github.com/DataDog/agent-payload/v5)
BuildRequires:  go(github.com/DataDog/appsec-internal-go)
BuildRequires:  go(github.com/DataDog/datadog-api-client-go)
BuildRequires:  go(github.com/DataDog/datadog-api-client-go/v2)
BuildRequires:  go(github.com/DataDog/datadog-go)
BuildRequires:  go(github.com/DataDog/datadog-go/v5)
BuildRequires:  go(github.com/DataDog/datadog-operator/api)
BuildRequires:  go(github.com/DataDog/datadog-traceroute)
BuildRequires:  go(github.com/DataDog/dd-trace-go/contrib/net/http/v2)
BuildRequires:  go(github.com/DataDog/dd-trace-go/v2)
BuildRequires:  go(github.com/DataDog/ddtrivy)
BuildRequires:  go(github.com/DataDog/ebpf-manager)
BuildRequires:  go(github.com/DataDog/go-acl)
BuildRequires:  go(github.com/DataDog/go-libddwaf/v3)
BuildRequires:  go(github.com/DataDog/go-libddwaf/v4)
BuildRequires:  go(github.com/DataDog/go-runtime-metrics-internal)
BuildRequires:  go(github.com/DataDog/go-sqllexer)
BuildRequires:  go(github.com/DataDog/go-tuf)
BuildRequires:  go(github.com/DataDog/gohai)
BuildRequires:  go(github.com/DataDog/jsonapi)
BuildRequires:  go(github.com/DataDog/mmh3)
BuildRequires:  go(github.com/DataDog/opentelemetry-mapping-go/pkg/otlp/attributes)
BuildRequires:  go(github.com/DataDog/orchestrion)
BuildRequires:  go(github.com/DataDog/rshell)
BuildRequires:  go(github.com/DataDog/sketches-go)
BuildRequires:  go(github.com/DataDog/viper)
BuildRequires:  go(github.com/DataDog/watermarkpodautoscaler/apis)
BuildRequires:  go(github.com/DataDog/zstd)
BuildRequires:  go(github.com/DataDog/zstd_0)
BuildRequires:  go(github.com/DisposaBoy/JsonConfigReader)
BuildRequires:  go(github.com/Djarvur/go-err113)
BuildRequires:  go(github.com/GoogleCloudPlatform/docker-credential-gcr)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp)
BuildRequires:  go(github.com/Jeffail/gabs/v2)
BuildRequires:  go(github.com/MakeNowJust/heredoc)
BuildRequires:  go(github.com/Masterminds/goutils)
BuildRequires:  go(github.com/Masterminds/semver)
BuildRequires:  go(github.com/Masterminds/semver/v3)
BuildRequires:  go(github.com/Masterminds/sprig/v3)
BuildRequires:  go(github.com/Microsoft/go-winio)
BuildRequires:  go(github.com/Microsoft/hcsshim)
BuildRequires:  go(github.com/MirrexOne/unqueryvet)
BuildRequires:  go(github.com/NVIDIA/go-nvml)
BuildRequires:  go(github.com/NYTimes/gziphandler)
BuildRequires:  go(github.com/OpenPeeDeeP/depguard/v2)
BuildRequires:  go(github.com/ProtonMail/go-crypto)
BuildRequires:  go(github.com/ProtonMail/gopenpgp/v3)
BuildRequires:  go(github.com/Showmax/go-fqdn)
BuildRequires:  go(github.com/VictoriaMetrics/easyproto)
BuildRequires:  go(github.com/aarzilli/whydeadcode)
BuildRequires:  go(github.com/aclements/go-moremath)
BuildRequires:  go(github.com/acobaugh/osrelease)
BuildRequires:  go(github.com/agext/levenshtein)
BuildRequires:  go(github.com/alecthomas/chroma/v2)
BuildRequires:  go(github.com/alecthomas/go-check-sumtype)
BuildRequires:  go(github.com/alecthomas/participle)
BuildRequires:  go(github.com/alecthomas/participle/v2)
BuildRequires:  go(github.com/alecthomas/repr)
BuildRequires:  go(github.com/alecthomas/units)
BuildRequires:  go(github.com/alessio/shellescape)
BuildRequires:  go(github.com/alexkohler/nakedret/v2)
BuildRequires:  go(github.com/alexkohler/prealloc)
BuildRequires:  go(github.com/alfatraining/structtag)
BuildRequires:  go(github.com/alingse/asasalint)
BuildRequires:  go(github.com/alingse/nilnesserr)
BuildRequires:  go(github.com/aliyun/alibaba-cloud-sdk-go)
BuildRequires:  go(github.com/antchfx/xmlquery)
BuildRequires:  go(github.com/antchfx/xpath)
BuildRequires:  go(github.com/antlr4-go/antlr/v4)
BuildRequires:  go(github.com/apache/thrift)
BuildRequires:  go(github.com/apparentlymart/go-textseg/v15)
BuildRequires:  go(github.com/aptly-dev/aptly)
BuildRequires:  go(github.com/aquasecurity/go-gem-version)
BuildRequires:  go(github.com/aquasecurity/go-npm-version)
BuildRequires:  go(github.com/aquasecurity/go-pep440-version)
BuildRequires:  go(github.com/aquasecurity/go-version)
BuildRequires:  go(github.com/aquasecurity/jfather)
BuildRequires:  go(github.com/aquasecurity/trivy)
BuildRequires:  go(github.com/aquasecurity/trivy-db)
BuildRequires:  go(github.com/aquasecurity/trivy-java-db)
BuildRequires:  go(github.com/armon/go-metrics)
BuildRequires:  go(github.com/armon/go-radix)
BuildRequires:  go(github.com/asaskevich/govalidator)
BuildRequires:  go(github.com/ashanbrown/forbidigo/v2)
BuildRequires:  go(github.com/ashanbrown/makezero/v2)
BuildRequires:  go(github.com/atotto/clipboard)
BuildRequires:  go(github.com/avast/retry-go/v4)
BuildRequires:  go(github.com/awalterschulze/gographviz)
BuildRequires:  go(github.com/aws/aws-sdk-go)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/config)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/credentials)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/feature/ec2/imds)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/configsources)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/endpoints/v2)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/v4a)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/ec2)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/ecr)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/ecs)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/eks)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/elasticache)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/checksum)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/presigned-url)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/s3shared)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/kafka)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/lightsail)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/rds)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/s3)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/secretsmanager)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/servicediscovery)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/signin)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/ssm)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/sso)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/ssooidc)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/sts)
BuildRequires:  go(github.com/aws/karpenter-provider-aws)
BuildRequires:  go(github.com/aws/session-manager-plugin)
BuildRequires:  go(github.com/aws/smithy-go)
BuildRequires:  go(github.com/awslabs/operatorpkg)
BuildRequires:  go(github.com/aymanbagabas/go-osc52/v2)
BuildRequires:  go(github.com/aymerick/raymond)
BuildRequires:  go(github.com/bahlo/generic-list-go)
BuildRequires:  go(github.com/bazelbuild/bazelisk)
BuildRequires:  go(github.com/bazelbuild/rules_go)
BuildRequires:  go(github.com/bboreham/go-loser)
BuildRequires:  go(github.com/beevik/ntp)
BuildRequires:  go(github.com/benbjohnson/clock)
BuildRequires:  go(github.com/benbjohnson/immutable)
BuildRequires:  go(github.com/beorn7/perks)
BuildRequires:  go(github.com/bgentry/go-netrc)
BuildRequires:  go(github.com/bgentry/speakeasy)
BuildRequires:  go(github.com/bhmj/jsonslice)
BuildRequires:  go(github.com/bhmj/xpression)
BuildRequires:  go(github.com/bitfield/gotestdox)
BuildRequires:  go(github.com/bitnami/go-version)
BuildRequires:  go(github.com/bkielbasa/cyclop)
BuildRequires:  go(github.com/blabber/go-freebsd-sysctl)
BuildRequires:  go(github.com/blakesmith/ar)
BuildRequires:  go(github.com/blang/semver)
BuildRequires:  go(github.com/blang/semver/v4)
BuildRequires:  go(github.com/blizzy78/varnamelen)
BuildRequires:  go(github.com/bmatcuk/doublestar/v4)
BuildRequires:  go(github.com/bmizerany/pat)
BuildRequires:  go(github.com/boltdb/bolt)
BuildRequires:  go(github.com/bombsimon/wsl/v4)
BuildRequires:  go(github.com/bombsimon/wsl/v5)
BuildRequires:  go(github.com/boombuler/barcode)
BuildRequires:  go(github.com/breml/bidichk)
BuildRequires:  go(github.com/breml/errchkjson)
BuildRequires:  go(github.com/briandowns/spinner)
BuildRequires:  go(github.com/brunoga/deep)
BuildRequires:  go(github.com/buger/jsonparser)
BuildRequires:  go(github.com/butuzov/ireturn)
BuildRequires:  go(github.com/butuzov/mirror)
BuildRequires:  go(github.com/catenacyber/perfsprint)
BuildRequires:  go(github.com/cavaliergopher/grab/v3)
BuildRequires:  go(github.com/ccojocar/zxcvbn-go)
BuildRequires:  go(github.com/cenkalti/backoff)
BuildRequires:  go(github.com/cenkalti/backoff/v4)
BuildRequires:  go(github.com/cenkalti/backoff/v5)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/chai2010/gettext-go)
BuildRequires:  go(github.com/charithe/durationcheck)
BuildRequires:  go(github.com/charlievieth/strcase)
BuildRequires:  go(github.com/charmbracelet/bubbles)
BuildRequires:  go(github.com/charmbracelet/bubbletea)
BuildRequires:  go(github.com/charmbracelet/colorprofile)
BuildRequires:  go(github.com/charmbracelet/lipgloss)
BuildRequires:  go(github.com/charmbracelet/ultraviolet)
BuildRequires:  go(github.com/charmbracelet/x/ansi)
BuildRequires:  go(github.com/charmbracelet/x/cellbuf)
BuildRequires:  go(github.com/charmbracelet/x/term)
BuildRequires:  go(github.com/charmbracelet/x/termios)
BuildRequires:  go(github.com/charmbracelet/x/windows)
BuildRequires:  go(github.com/cheggaaa/pb)
BuildRequires:  go(github.com/chrusty/protoc-gen-jsonschema)
BuildRequires:  go(github.com/cihub/seelog)
BuildRequires:  go(github.com/cilium/ebpf)
BuildRequires:  go(github.com/circonus-labs/circonus-gometrics)
BuildRequires:  go(github.com/circonus-labs/circonusllhist)
BuildRequires:  go(github.com/ckaznocha/intrange)
BuildRequires:  go(github.com/clbanning/mxj)
BuildRequires:  go(github.com/clipperhouse/displaywidth)
BuildRequires:  go(github.com/clipperhouse/stringish)
BuildRequires:  go(github.com/clipperhouse/uax29/v2)
BuildRequires:  go(github.com/cloudflare/cbpfc)
BuildRequires:  go(github.com/cloudflare/circl)
BuildRequires:  go(github.com/cloudfoundry-community/go-cfclient/v2)
BuildRequires:  go(github.com/cncf/xds/go)
BuildRequires:  go(github.com/containerd/cgroups/v3)
BuildRequires:  go(github.com/containerd/containerd)
BuildRequires:  go(github.com/containerd/containerd/api)
BuildRequires:  go(github.com/containerd/continuity)
BuildRequires:  go(github.com/containerd/errdefs)
BuildRequires:  go(github.com/containerd/errdefs/pkg)
BuildRequires:  go(github.com/containerd/fifo)
BuildRequires:  go(github.com/containerd/log)
BuildRequires:  go(github.com/containerd/platforms)
BuildRequires:  go(github.com/containerd/stargz-snapshotter/estargz)
BuildRequires:  go(github.com/containerd/ttrpc)
BuildRequires:  go(github.com/containerd/typeurl/v2)
BuildRequires:  go(github.com/containernetworking/cni)
BuildRequires:  go(github.com/containernetworking/plugins)
BuildRequires:  go(github.com/coreos/etcd)
BuildRequires:  go(github.com/coreos/go-semver)
BuildRequires:  go(github.com/coreos/go-systemd)
BuildRequires:  go(github.com/coreos/go-systemd/v22)
BuildRequires:  go(github.com/coreos/pkg)
BuildRequires:  go(github.com/cpuguy83/go-md2man/v2)
BuildRequires:  go(github.com/creack/pty)
BuildRequires:  go(github.com/cri-o/ocicni)
BuildRequires:  go(github.com/curioswitch/go-reassign)
BuildRequires:  go(github.com/cyphar/filepath-securejoin)
BuildRequires:  go(github.com/daixiang0/gci)
BuildRequires:  go(github.com/dave/dst)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/decred/dcrd/dcrec/secp256k1/v4)
BuildRequires:  go(github.com/denis-tingaikin/go-header)
BuildRequires:  go(github.com/dennwc/varint)
BuildRequires:  go(github.com/denverdino/aliyungo)
BuildRequires:  go(github.com/dgryski/go-farm)
BuildRequires:  go(github.com/dgryski/go-jump)
BuildRequires:  go(github.com/dgryski/go-minhash)
BuildRequires:  go(github.com/dgryski/go-rendezvous)
BuildRequires:  go(github.com/digitalocean/go-libvirt)
BuildRequires:  go(github.com/digitalocean/go-metadata)
BuildRequires:  go(github.com/digitalocean/godo)
BuildRequires:  go(github.com/dimchansky/utfbom)
BuildRequires:  go(github.com/distribution/reference)
BuildRequires:  go(github.com/djherbis/times)
BuildRequires:  go(github.com/dlclark/regexp2)
BuildRequires:  go(github.com/dnephin/pflag)
BuildRequires:  go(github.com/docker/cli)
BuildRequires:  go(github.com/docker/docker)
BuildRequires:  go(github.com/docker/docker-credential-helpers)
BuildRequires:  go(github.com/docker/go-connections)
BuildRequires:  go(github.com/docker/go-events)
BuildRequires:  go(github.com/docker/go-units)
BuildRequires:  go(github.com/duosecurity/duo_api_golang)
BuildRequires:  go(github.com/dustin/go-humanize)
BuildRequires:  go(github.com/eapache/queue/v2)
BuildRequires:  go(github.com/ebitengine/purego)
BuildRequires:  go(github.com/edsrzf/mmap-go)
BuildRequires:  go(github.com/ekzhu/minhash-lsh)
BuildRequires:  go(github.com/elastic/go-freelru)
BuildRequires:  go(github.com/elastic/go-grok)
BuildRequires:  go(github.com/elastic/go-libaudit/v2)
BuildRequires:  go(github.com/elastic/go-licenser)
BuildRequires:  go(github.com/elastic/go-perf)
BuildRequires:  go(github.com/elastic/go-seccomp-bpf)
BuildRequires:  go(github.com/elastic/lunes)
BuildRequires:  go(github.com/emicklei/dot)
BuildRequires:  go(github.com/emicklei/go-restful/v3)
BuildRequires:  go(github.com/emirpasic/gods)
BuildRequires:  go(github.com/envoyproxy/gateway)
BuildRequires:  go(github.com/envoyproxy/go-control-plane/envoy)
BuildRequires:  go(github.com/envoyproxy/protoc-gen-validate)
BuildRequires:  go(github.com/erikgeiser/coninput)
BuildRequires:  go(github.com/ettle/strcase)
BuildRequires:  go(github.com/evanphx/json-patch)
BuildRequires:  go(github.com/evanphx/json-patch/v5)
BuildRequires:  go(github.com/exponent-io/jsonpath)
BuildRequires:  go(github.com/expr-lang/expr)
BuildRequires:  go(github.com/facebookgo/clock)
BuildRequires:  go(github.com/facette/natsort)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/fatih/structs)
BuildRequires:  go(github.com/fatih/structtag)
BuildRequires:  go(github.com/favadi/protoc-go-inject-tag)
BuildRequires:  go(github.com/felixge/fgprof)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/firefart/nonamedreturns)
BuildRequires:  go(github.com/foxboron/go-tpm-keyfiles)
BuildRequires:  go(github.com/frapposelli/wwhrd)
BuildRequires:  go(github.com/freddierice/go-losetup)
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/fxamacker/cbor/v2)
BuildRequires:  go(github.com/fzipp/gocyclo)
BuildRequires:  go(github.com/gammazero/deque)
BuildRequires:  go(github.com/gammazero/workerpool)
BuildRequires:  go(github.com/ghodss/yaml)
BuildRequires:  go(github.com/ghostiam/protogetter)
BuildRequires:  go(github.com/glaslos/ssdeep)
BuildRequires:  go(github.com/glebarez/go-sqlite)
BuildRequires:  go(github.com/go-critic/go-critic)
BuildRequires:  go(github.com/go-delve/delve)
BuildRequires:  go(github.com/go-enry/go-license-detector/v4)
BuildRequires:  go(github.com/go-errors/errors)
BuildRequires:  go(github.com/go-git/gcfg)
BuildRequires:  go(github.com/go-git/go-billy/v5)
BuildRequires:  go(github.com/go-git/go-git/v5)
BuildRequires:  go(github.com/go-ini/ini)
BuildRequires:  go(github.com/go-jose/go-jose/v3)
BuildRequires:  go(github.com/go-jose/go-jose/v4)
BuildRequires:  go(github.com/go-json-experiment/json)
BuildRequires:  go(github.com/go-kit/log)
BuildRequires:  go(github.com/go-logfmt/logfmt)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/go-logr/zapr)
BuildRequires:  go(github.com/go-ole/go-ole)
BuildRequires:  go(github.com/go-openapi/analysis)
BuildRequires:  go(github.com/go-openapi/errors)
BuildRequires:  go(github.com/go-openapi/jsonpointer)
BuildRequires:  go(github.com/go-openapi/jsonreference)
BuildRequires:  go(github.com/go-openapi/loads)
BuildRequires:  go(github.com/go-openapi/spec)
BuildRequires:  go(github.com/go-openapi/strfmt)
BuildRequires:  go(github.com/go-openapi/swag)
BuildRequires:  go(github.com/go-openapi/swag/cmdutils)
BuildRequires:  go(github.com/go-openapi/swag/conv)
BuildRequires:  go(github.com/go-openapi/swag/fileutils)
BuildRequires:  go(github.com/go-openapi/swag/jsonname)
BuildRequires:  go(github.com/go-openapi/swag/jsonutils)
BuildRequires:  go(github.com/go-openapi/swag/loading)
BuildRequires:  go(github.com/go-openapi/swag/mangling)
BuildRequires:  go(github.com/go-openapi/swag/netutils)
BuildRequires:  go(github.com/go-openapi/swag/stringutils)
BuildRequires:  go(github.com/go-openapi/swag/typeutils)
BuildRequires:  go(github.com/go-openapi/swag/yamlutils)
BuildRequires:  go(github.com/go-openapi/testify/enable/yaml/v2)
BuildRequires:  go(github.com/go-openapi/testify/v2)
BuildRequires:  go(github.com/go-openapi/validate)
BuildRequires:  go(github.com/go-ozzo/ozzo-validation)
BuildRequires:  go(github.com/go-quicktest/qt)
BuildRequires:  go(github.com/go-redis/redis/v8)
BuildRequires:  go(github.com/go-resty/resty/v2)
BuildRequires:  go(github.com/go-sql-driver/mysql)
BuildRequires:  go(github.com/go-test/deep)
BuildRequires:  go(github.com/go-toolsmith/astcast)
BuildRequires:  go(github.com/go-toolsmith/astcopy)
BuildRequires:  go(github.com/go-toolsmith/astequal)
BuildRequires:  go(github.com/go-toolsmith/astfmt)
BuildRequires:  go(github.com/go-toolsmith/astp)
BuildRequires:  go(github.com/go-toolsmith/strparse)
BuildRequires:  go(github.com/go-toolsmith/typep)
BuildRequires:  go(github.com/go-viper/mapstructure/v2)
BuildRequires:  go(github.com/go-xmlfmt/xmlfmt)
BuildRequires:  go(github.com/go-zookeeper/zk)
BuildRequires:  go(github.com/gobuffalo/flect)
BuildRequires:  go(github.com/gobwas/glob)
BuildRequires:  go(github.com/goccy/go-json)
BuildRequires:  go(github.com/goccy/go-yaml)
BuildRequires:  go(github.com/gocomply/scap)
BuildRequires:  go(github.com/gocql/gocql)
BuildRequires:  go(github.com/godbus/dbus)
BuildRequires:  go(github.com/godbus/dbus/v5)
BuildRequires:  go(github.com/godoc-lint/godoc-lint)
BuildRequires:  go(github.com/godror/godror)
BuildRequires:  go(github.com/godror/knownpb)
BuildRequires:  go(github.com/gofrs/flock)
BuildRequires:  go(github.com/gofrs/uuid)
BuildRequires:  go(github.com/gogo/googleapis)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/golang-jwt/jwt/v4)
BuildRequires:  go(github.com/golang-jwt/jwt/v5)
BuildRequires:  go(github.com/golang/glog)
BuildRequires:  go(github.com/golang/groupcache)
BuildRequires:  go(github.com/golang/mock)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/golang/snappy)
BuildRequires:  go(github.com/golangci/asciicheck)
BuildRequires:  go(github.com/golangci/dupl)
BuildRequires:  go(github.com/golangci/go-printf-func-name)
BuildRequires:  go(github.com/golangci/gofmt)
BuildRequires:  go(github.com/golangci/golangci-lint/v2)
BuildRequires:  go(github.com/golangci/golines)
BuildRequires:  go(github.com/golangci/misspell)
BuildRequires:  go(github.com/golangci/plugin-module-register)
BuildRequires:  go(github.com/golangci/revgrep)
BuildRequires:  go(github.com/golangci/rowserrcheck)
BuildRequires:  go(github.com/golangci/swaggoswag)
BuildRequires:  go(github.com/golangci/unconvert)
BuildRequires:  go(github.com/google/btree)
BuildRequires:  go(github.com/google/cel-go)
BuildRequires:  go(github.com/google/certificate-transparency-go)
BuildRequires:  go(github.com/google/gnostic-models)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-containerregistry)
BuildRequires:  go(github.com/google/go-intervals)
BuildRequires:  go(github.com/google/go-metrics-stackdriver)
BuildRequires:  go(github.com/google/go-querystring)
BuildRequires:  go(github.com/google/go-tpm)
BuildRequires:  go(github.com/google/gofuzz)
BuildRequires:  go(github.com/google/gopacket)
BuildRequires:  go(github.com/google/jsonschema-go)
BuildRequires:  go(github.com/google/licensecheck)
BuildRequires:  go(github.com/google/pprof)
BuildRequires:  go(github.com/google/s2a-go)
BuildRequires:  go(github.com/google/shlex)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/google/wire)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(github.com/gophercloud/gophercloud)
BuildRequires:  go(github.com/gophercloud/gophercloud/v2)
BuildRequires:  go(github.com/gopherjs/gopherjs)
BuildRequires:  go(github.com/gordonklaus/ineffassign)
BuildRequires:  go(github.com/gorilla/handlers)
BuildRequires:  go(github.com/gorilla/mux)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/gosnmp/gosnmp)
BuildRequires:  go(github.com/gostaticanalysis/analysisutil)
BuildRequires:  go(github.com/gostaticanalysis/comment)
BuildRequires:  go(github.com/gostaticanalysis/forcetypeassert)
BuildRequires:  go(github.com/gostaticanalysis/nilerr)
BuildRequires:  go(github.com/goware/modvendor)
BuildRequires:  go(github.com/grafana/regexp)
BuildRequires:  go(github.com/gregjones/httpcache)
BuildRequires:  go(github.com/grpc-ecosystem/go-grpc-middleware)
BuildRequires:  go(github.com/grpc-ecosystem/go-grpc-middleware/v2)
BuildRequires:  go(github.com/grpc-ecosystem/go-grpc-prometheus)
BuildRequires:  go(github.com/grpc-ecosystem/grpc-gateway/v2)
BuildRequires:  go(github.com/grpc-ecosystem/grpc-opentracing)
BuildRequires:  go(github.com/gsterjov/go-libsecret)
BuildRequires:  go(github.com/h2non/filetype)
BuildRequires:  go(github.com/hairyhenderson/go-codeowners)
BuildRequires:  go(github.com/hashicorp/cli)
BuildRequires:  go(github.com/hashicorp/consul/api)
BuildRequires:  go(github.com/hashicorp/consul/sdk)
BuildRequires:  go(github.com/hashicorp/cronexpr)
BuildRequires:  go(github.com/hashicorp/errwrap)
BuildRequires:  go(github.com/hashicorp/eventlogger)
BuildRequires:  go(github.com/hashicorp/go-bexpr)
BuildRequires:  go(github.com/hashicorp/go-cleanhttp)
BuildRequires:  go(github.com/hashicorp/go-discover)
BuildRequires:  go(github.com/hashicorp/go-discover/provider/gce)
BuildRequires:  go(github.com/hashicorp/go-hclog)
BuildRequires:  go(github.com/hashicorp/go-hmac-drbg)
BuildRequires:  go(github.com/hashicorp/go-immutable-radix)
BuildRequires:  go(github.com/hashicorp/go-immutable-radix/v2)
BuildRequires:  go(github.com/hashicorp/go-kms-wrapping/entropy/v2)
BuildRequires:  go(github.com/hashicorp/go-kms-wrapping/v2)
BuildRequires:  go(github.com/hashicorp/go-kms-wrapping/wrappers/aead/v2)
BuildRequires:  go(github.com/hashicorp/go-kms-wrapping/wrappers/alicloudkms/v2)
BuildRequires:  go(github.com/hashicorp/go-kms-wrapping/wrappers/awskms/v2)
BuildRequires:  go(github.com/hashicorp/go-kms-wrapping/wrappers/azurekeyvault/v2)
BuildRequires:  go(github.com/hashicorp/go-kms-wrapping/wrappers/gcpckms/v2)
BuildRequires:  go(github.com/hashicorp/go-kms-wrapping/wrappers/ocikms/v2)
BuildRequires:  go(github.com/hashicorp/go-kms-wrapping/wrappers/transit/v2)
BuildRequires:  go(github.com/hashicorp/go-memdb)
BuildRequires:  go(github.com/hashicorp/go-metrics)
BuildRequires:  go(github.com/hashicorp/go-msgpack/v2)
BuildRequires:  go(github.com/hashicorp/go-multierror)
BuildRequires:  go(github.com/hashicorp/go-plugin)
BuildRequires:  go(github.com/hashicorp/go-raftchunking)
BuildRequires:  go(github.com/hashicorp/go-retryablehttp)
BuildRequires:  go(github.com/hashicorp/go-rootcerts)
BuildRequires:  go(github.com/hashicorp/go-secure-stdlib/awsutil)
BuildRequires:  go(github.com/hashicorp/go-secure-stdlib/base62)
BuildRequires:  go(github.com/hashicorp/go-secure-stdlib/cryptoutil)
BuildRequires:  go(github.com/hashicorp/go-secure-stdlib/mlock)
BuildRequires:  go(github.com/hashicorp/go-secure-stdlib/parseutil)
BuildRequires:  go(github.com/hashicorp/go-secure-stdlib/permitpool)
BuildRequires:  go(github.com/hashicorp/go-secure-stdlib/plugincontainer)
BuildRequires:  go(github.com/hashicorp/go-secure-stdlib/regexp)
BuildRequires:  go(github.com/hashicorp/go-secure-stdlib/reloadutil)
BuildRequires:  go(github.com/hashicorp/go-secure-stdlib/strutil)
BuildRequires:  go(github.com/hashicorp/go-secure-stdlib/tlsutil)
BuildRequires:  go(github.com/hashicorp/go-sockaddr)
BuildRequires:  go(github.com/hashicorp/go-syslog)
BuildRequires:  go(github.com/hashicorp/go-uuid)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/hashicorp/golang-lru)
BuildRequires:  go(github.com/hashicorp/golang-lru/v2)
BuildRequires:  go(github.com/hashicorp/hcl)
BuildRequires:  go(github.com/hashicorp/hcl/v2)
BuildRequires:  go(github.com/hashicorp/hcp-sdk-go)
BuildRequires:  go(github.com/hashicorp/mdns)
BuildRequires:  go(github.com/hashicorp/nomad/api)
BuildRequires:  go(github.com/hashicorp/raft)
BuildRequires:  go(github.com/hashicorp/raft-autopilot)
BuildRequires:  go(github.com/hashicorp/raft-boltdb/v2)
BuildRequires:  go(github.com/hashicorp/raft-snapshot)
BuildRequires:  go(github.com/hashicorp/raft-wal)
BuildRequires:  go(github.com/hashicorp/serf)
BuildRequires:  go(github.com/hashicorp/vault)
BuildRequires:  go(github.com/hashicorp/vault-plugin-secrets-kv)
BuildRequires:  go(github.com/hashicorp/vault/api)
BuildRequires:  go(github.com/hashicorp/vault/api/auth/approle)
BuildRequires:  go(github.com/hashicorp/vault/api/auth/aws)
BuildRequires:  go(github.com/hashicorp/vault/api/auth/ldap)
BuildRequires:  go(github.com/hashicorp/vault/api/auth/userpass)
BuildRequires:  go(github.com/hashicorp/vault/sdk)
BuildRequires:  go(github.com/hashicorp/vic)
BuildRequires:  go(github.com/hashicorp/yamux)
BuildRequires:  go(github.com/hetznercloud/hcloud-go/v2)
BuildRequires:  go(github.com/hexops/gotextdiff)
BuildRequires:  go(github.com/hhatto/gorst)
BuildRequires:  go(github.com/huandu/xstrings)
BuildRequires:  go(github.com/iancoleman/strcase)
BuildRequires:  go(github.com/iceber/iouring-go)
BuildRequires:  go(github.com/imdario/mergo)
BuildRequires:  go(github.com/inconshreveable/mousetrap)
BuildRequires:  go(github.com/invopop/jsonschema)
BuildRequires:  go(github.com/ionos-cloud/sdk-go/v6)
BuildRequires:  go(github.com/itchyny/gojq)
BuildRequires:  go(github.com/itchyny/timefmt-go)
BuildRequires:  go(github.com/iwdgo/sigintwindows)
BuildRequires:  go(github.com/jackc/chunkreader/v2)
BuildRequires:  go(github.com/jackc/pgconn)
BuildRequires:  go(github.com/jackc/pgio)
BuildRequires:  go(github.com/jackc/pgpassfile)
BuildRequires:  go(github.com/jackc/pgproto3/v2)
BuildRequires:  go(github.com/jackc/pgservicefile)
BuildRequires:  go(github.com/jackc/pgtype)
BuildRequires:  go(github.com/jackc/pgx/v4)
BuildRequires:  go(github.com/jackc/pgx/v5)
BuildRequires:  go(github.com/jackc/puddle/v2)
BuildRequires:  go(github.com/jaegertracing/jaeger-idl)
BuildRequires:  go(github.com/jarcoal/httpmock)
BuildRequires:  go(github.com/jbenet/go-context)
BuildRequires:  go(github.com/jdkato/prose)
BuildRequires:  go(github.com/jedib0t/go-pretty/v6)
BuildRequires:  go(github.com/jefferai/isbadcipher)
BuildRequires:  go(github.com/jefferai/jsonx)
BuildRequires:  go(github.com/jellydator/ttlcache/v3)
BuildRequires:  go(github.com/jessevdk/go-flags)
BuildRequires:  go(github.com/jgautheron/goconst)
BuildRequires:  go(github.com/jinzhu/inflection)
BuildRequires:  go(github.com/jjti/go-spancheck)
BuildRequires:  go(github.com/jlaffaye/ftp)
BuildRequires:  go(github.com/jmespath/go-jmespath)
BuildRequires:  go(github.com/jmoiron/sqlx)
BuildRequires:  go(github.com/jonboulle/clockwork)
BuildRequires:  go(github.com/josharian/intern)
BuildRequires:  go(github.com/joshlf/go-acl)
BuildRequires:  go(github.com/joyent/triton-go)
BuildRequires:  go(github.com/jpillora/backoff)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/judwhite/go-svc)
BuildRequires:  go(github.com/julienschmidt/httprouter)
BuildRequires:  go(github.com/julz/importas)
BuildRequires:  go(github.com/justincormack/go-memfd)
BuildRequires:  go(github.com/karamaru-alpha/copyloopvar)
BuildRequires:  go(github.com/kballard/go-shellquote)
BuildRequires:  go(github.com/kelseyhightower/envconfig)
BuildRequires:  go(github.com/kevinburke/ssh_config)
BuildRequires:  go(github.com/kisielk/errcheck)
BuildRequires:  go(github.com/kjk/lzma)
BuildRequires:  go(github.com/kkHAIKE/contextcheck)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/klauspost/cpuid/v2)
BuildRequires:  go(github.com/klauspost/pgzip)
BuildRequires:  go(github.com/knadh/koanf/maps)
BuildRequires:  go(github.com/knadh/koanf/parsers/yaml)
BuildRequires:  go(github.com/knadh/koanf/providers/confmap)
BuildRequires:  go(github.com/knadh/koanf/providers/env)
BuildRequires:  go(github.com/knadh/koanf/providers/file)
BuildRequires:  go(github.com/knadh/koanf/providers/posflag)
BuildRequires:  go(github.com/knadh/koanf/providers/structs)
BuildRequires:  go(github.com/knadh/koanf/v2)
BuildRequires:  go(github.com/knqyf263/go-apk-version)
BuildRequires:  go(github.com/knqyf263/go-deb-version)
BuildRequires:  go(github.com/knqyf263/go-rpm-version)
BuildRequires:  go(github.com/knqyf263/go-rpmdb)
BuildRequires:  go(github.com/knqyf263/nested)
BuildRequires:  go(github.com/kolo/xmlrpc)
BuildRequires:  go(github.com/kouhin/envflag)
BuildRequires:  go(github.com/kr/fs)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/kraken-hpc/go-fork)
BuildRequires:  go(github.com/kulti/thelper)
BuildRequires:  go(github.com/kunwardeep/paralleltest)
BuildRequires:  go(github.com/kylelemons/godebug)
BuildRequires:  go(github.com/lasiar/canonicalheader)
BuildRequires:  go(github.com/ldez/exptostd)
BuildRequires:  go(github.com/ldez/gomoddirectives)
BuildRequires:  go(github.com/ldez/grignotin)
BuildRequires:  go(github.com/ldez/structtags)
BuildRequires:  go(github.com/ldez/tagliatelle)
BuildRequires:  go(github.com/ldez/usetesting)
BuildRequires:  go(github.com/leodido/go-syslog/v4)
BuildRequires:  go(github.com/leodido/ragel-machinery)
BuildRequires:  go(github.com/leonklingele/grouper)
BuildRequires:  go(github.com/lestrrat-go/backoff/v2)
BuildRequires:  go(github.com/lestrrat-go/blackmagic)
BuildRequires:  go(github.com/lestrrat-go/httpcc)
BuildRequires:  go(github.com/lestrrat-go/iter)
BuildRequires:  go(github.com/lestrrat-go/jwx)
BuildRequires:  go(github.com/lestrrat-go/option)
BuildRequires:  go(github.com/libp2p/go-reuseport)
BuildRequires:  go(github.com/liggitt/tabwriter)
BuildRequires:  go(github.com/lightstep/go-expohisto)
BuildRequires:  go(github.com/linkdata/deadlock)
BuildRequires:  go(github.com/linode/go-metadata)
BuildRequires:  go(github.com/linode/linodego)
BuildRequires:  go(github.com/lorenzosaino/go-sysctl)
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)
BuildRequires:  go(github.com/lufia/plan9stats)
BuildRequires:  go(github.com/lunixbochs/struc)
BuildRequires:  go(github.com/lxn/walk)
BuildRequires:  go(github.com/lxn/win)
BuildRequires:  go(github.com/macabu/inamedparam)
BuildRequires:  go(github.com/magefile/mage)
BuildRequires:  go(github.com/magiconair/properties)
BuildRequires:  go(github.com/mailru/easyjson)
BuildRequires:  go(github.com/manuelarte/embeddedstructfieldcheck)
BuildRequires:  go(github.com/manuelarte/funcorder)
BuildRequires:  go(github.com/maratori/testableexamples)
BuildRequires:  go(github.com/maratori/testpackage)
BuildRequires:  go(github.com/masahiro331/go-disk)
BuildRequires:  go(github.com/masahiro331/go-ext4-filesystem)
BuildRequires:  go(github.com/masahiro331/go-mvn-version)
BuildRequires:  go(github.com/masahiro331/go-xfs-filesystem)
BuildRequires:  go(github.com/matoous/godox)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/mattn/go-localereader)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/mattn/go-shellwords)
BuildRequires:  go(github.com/mattn/go-sqlite3)
BuildRequires:  go(github.com/mattn/go-zglob)
BuildRequires:  go(github.com/maxatome/go-testdeep)
BuildRequires:  go(github.com/mdlayher/kobject)
BuildRequires:  go(github.com/mdlayher/netlink)
BuildRequires:  go(github.com/mdlayher/socket)
BuildRequires:  go(github.com/mdlayher/vsock)
BuildRequires:  go(github.com/mgechev/revive)
BuildRequires:  go(github.com/miekg/dns)
BuildRequires:  go(github.com/minio/highwayhash)
BuildRequires:  go(github.com/minio/sha256-simd)
BuildRequires:  go(github.com/minio/simdjson-go)
BuildRequires:  go(github.com/mitchellh/copystructure)
BuildRequires:  go(github.com/mitchellh/go-homedir)
BuildRequires:  go(github.com/mitchellh/go-ps)
BuildRequires:  go(github.com/mitchellh/go-wordwrap)
BuildRequires:  go(github.com/mitchellh/hashstructure/v2)
BuildRequires:  go(github.com/mitchellh/mapstructure)
BuildRequires:  go(github.com/mitchellh/pointerstructure)
BuildRequires:  go(github.com/mitchellh/reflectwalk)
BuildRequires:  go(github.com/mkrautz/goar)
BuildRequires:  go(github.com/moby/docker-image-spec)
BuildRequires:  go(github.com/moby/locker)
BuildRequires:  go(github.com/moby/moby/api)
BuildRequires:  go(github.com/moby/moby/client)
BuildRequires:  go(github.com/moby/spdystream)
BuildRequires:  go(github.com/moby/sys/mountinfo)
BuildRequires:  go(github.com/moby/sys/sequential)
BuildRequires:  go(github.com/moby/sys/signal)
BuildRequires:  go(github.com/moby/sys/user)
BuildRequires:  go(github.com/moby/sys/userns)
BuildRequires:  go(github.com/moby/term)
BuildRequires:  go(github.com/modelcontextprotocol/go-sdk)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/mohae/deepcopy)
BuildRequires:  go(github.com/monochromegane/go-gitignore)
BuildRequires:  go(github.com/montanaflynn/stats)
BuildRequires:  go(github.com/moricho/tparallel)
BuildRequires:  go(github.com/muesli/ansi)
BuildRequires:  go(github.com/muesli/cancelreader)
BuildRequires:  go(github.com/muesli/termenv)
BuildRequires:  go(github.com/munnerz/goautoneg)
BuildRequires:  go(github.com/mwitkow/go-conntrack)
BuildRequires:  go(github.com/mxk/go-flowrate)
BuildRequires:  go(github.com/nakabonne/nestif)
BuildRequires:  go(github.com/nats-io/jwt/v2)
BuildRequires:  go(github.com/nats-io/nats-server/v2)
BuildRequires:  go(github.com/nats-io/nats.go)
BuildRequires:  go(github.com/nats-io/nkeys)
BuildRequires:  go(github.com/nats-io/nuid)
BuildRequires:  go(github.com/netsampler/goflow2)
BuildRequires:  go(github.com/nexus-rpc/sdk-go)
BuildRequires:  go(github.com/nicolai86/scaleway-sdk)
BuildRequires:  go(github.com/nishanths/exhaustive)
BuildRequires:  go(github.com/nishanths/predeclared)
BuildRequires:  go(github.com/nu7hatch/gouuid)
BuildRequires:  go(github.com/nunnatsa/ginkgolinter)
BuildRequires:  go(github.com/nxadm/tail)
BuildRequires:  go(github.com/oklog/run)
BuildRequires:  go(github.com/oklog/ulid/v2)
BuildRequires:  go(github.com/okta/okta-sdk-golang/v5)
BuildRequires:  go(github.com/oliveagle/jsonpath)
BuildRequires:  go(github.com/onsi/ginkgo/v2)
BuildRequires:  go(github.com/onsi/gomega)
BuildRequires:  go(github.com/open-policy-agent/opa)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/routingconnector)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/spanmetricsconnector)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/loadbalancingexporter)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/datadogextension)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/healthcheckextension)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/k8sleaderelector)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer/dockerobserver)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer/ecsobserver)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer/hostobserver)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer/k8sobserver)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/pprofextension)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/storage/filestorage)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/aws/ecsutil)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/common)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/coreinternal)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/datadog)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/docker)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/exp/metrics)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/filter)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/gopsutilenv)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/healthcheck)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/k8sconfig)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/k8sinventory)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/metadataproviders)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/pdatautil)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/sharedcomponent)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/batchpersignal)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/core/xidutils)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/datadog)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/experimentalmetricmetadata)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/pdatatest)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/pdatautil)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/resourcetotelemetry)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/sampling)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/status)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/jaeger)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/prometheus)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/zipkin)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/winperfcounters)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/attributesprocessor)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/cumulativetodeltaprocessor)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatocumulativeprocessor)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/filterprocessor)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/groupbyattrsprocessor)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/k8sattributesprocessor)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/probabilisticsamplerprocessor)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourceprocessor)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/tailsamplingprocessor)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/transformprocessor)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/filelogreceiver)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/fluentforwardreceiver)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/jaegerreceiver)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sobjectsreceiver)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/prometheusreceiver)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/receivercreator)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/zipkinreceiver)
BuildRequires:  go(github.com/opencontainers/go-digest)
BuildRequires:  go(github.com/opencontainers/image-spec)
BuildRequires:  go(github.com/opencontainers/runtime-spec)
BuildRequires:  go(github.com/opencontainers/selinux)
BuildRequires:  go(github.com/openshift/api)
BuildRequires:  go(github.com/openshift/client-go)
BuildRequires:  go(github.com/opentracing/basictracer-go)
BuildRequires:  go(github.com/opentracing/opentracing-go)
BuildRequires:  go(github.com/openzipkin/zipkin-go)
BuildRequires:  go(github.com/oracle/oci-go-sdk/v60)
BuildRequires:  go(github.com/otiai10/copy)
BuildRequires:  go(github.com/outcaste-io/ristretto)
BuildRequires:  go(github.com/outscale/osc-sdk-go/v2)
BuildRequires:  go(github.com/ovh/go-ovh)
BuildRequires:  go(github.com/package-url/packageurl-go)
BuildRequires:  go(github.com/packethost/packngo)
BuildRequires:  go(github.com/pahanini/go-grpc-bidirectional-streaming-example)
BuildRequires:  go(github.com/patrickmn/go-cache)
BuildRequires:  go(github.com/pb33f/jsonpath)
BuildRequires:  go(github.com/pb33f/libopenapi)
BuildRequires:  go(github.com/pb33f/ordered-map/v2)
BuildRequires:  go(github.com/pelletier/go-toml)
BuildRequires:  go(github.com/pelletier/go-toml/v2)
BuildRequires:  go(github.com/peterbourgon/diskv)
BuildRequires:  go(github.com/petermattis/goid)
BuildRequires:  go(github.com/pgavlin/fx)
BuildRequires:  go(github.com/philhofer/fwd)
BuildRequires:  go(github.com/pierrec/lz4)
BuildRequires:  go(github.com/pierrec/lz4/v4)
BuildRequires:  go(github.com/pires/go-proxyproto)
BuildRequires:  go(github.com/pjbgf/sha1cd)
BuildRequires:  go(github.com/pkg/browser)
BuildRequires:  go(github.com/pkg/diff)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/pkg/sftp)
BuildRequires:  go(github.com/pkg/term)
BuildRequires:  go(github.com/planetscale/vtprotobuf)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/posener/complete)
BuildRequires:  go(github.com/power-devops/perfstat)
BuildRequires:  go(github.com/pquerna/otp)
BuildRequires:  go(github.com/prometheus-community/pro-bing)
BuildRequires:  go(github.com/prometheus/alertmanager)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_golang/exp)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/common/assets)
BuildRequires:  go(github.com/prometheus/exporter-toolkit)
BuildRequires:  go(github.com/prometheus/otlptranslator)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(github.com/prometheus/prometheus)
BuildRequires:  go(github.com/prometheus/sigv4)
BuildRequires:  go(github.com/protocolbuffers/protoscope)
BuildRequires:  go(github.com/pulumi/appdash)
BuildRequires:  go(github.com/pulumi/esc)
BuildRequires:  go(github.com/pulumi/pulumi-aws/sdk/v7)
BuildRequires:  go(github.com/pulumi/pulumi-awsx/sdk/v3)
BuildRequires:  go(github.com/pulumi/pulumi-azure-native-sdk/authorization/v2)
BuildRequires:  go(github.com/pulumi/pulumi-azure-native-sdk/compute/v2)
BuildRequires:  go(github.com/pulumi/pulumi-azure-native-sdk/containerservice/v2)
BuildRequires:  go(github.com/pulumi/pulumi-azure-native-sdk/managedidentity/v2)
BuildRequires:  go(github.com/pulumi/pulumi-azure-native-sdk/network/v2)
BuildRequires:  go(github.com/pulumi/pulumi-azure-native-sdk/v2)
BuildRequires:  go(github.com/pulumi/pulumi-command/sdk)
BuildRequires:  go(github.com/pulumi/pulumi-docker-build/sdk/go/dockerbuild)
BuildRequires:  go(github.com/pulumi/pulumi-docker/sdk/v4)
BuildRequires:  go(github.com/pulumi/pulumi-eks/sdk/v4)
BuildRequires:  go(github.com/pulumi/pulumi-gcp/sdk/v7)
BuildRequires:  go(github.com/pulumi/pulumi-kubernetes/sdk/v4)
BuildRequires:  go(github.com/pulumi/pulumi-libvirt/sdk)
BuildRequires:  go(github.com/pulumi/pulumi-random/sdk/v4)
BuildRequires:  go(github.com/pulumi/pulumi-tls/sdk/v4)
BuildRequires:  go(github.com/pulumi/pulumi/sdk/v3)
BuildRequires:  go(github.com/pulumiverse/pulumi-time/sdk)
BuildRequires:  go(github.com/puzpuzpuz/xsync/v3)
BuildRequires:  go(github.com/puzpuzpuz/xsync/v4)
BuildRequires:  go(github.com/qri-io/jsonpointer)
BuildRequires:  go(github.com/quasilyte/go-ruleguard)
BuildRequires:  go(github.com/quasilyte/go-ruleguard/dsl)
BuildRequires:  go(github.com/quasilyte/gogrep)
BuildRequires:  go(github.com/quasilyte/regex/syntax)
BuildRequires:  go(github.com/quasilyte/stdinfo)
BuildRequires:  go(github.com/raeperd/recvcheck)
BuildRequires:  go(github.com/rboyer/safeio)
BuildRequires:  go(github.com/rcrowley/go-metrics)
BuildRequires:  go(github.com/redis/go-redis/v9)
BuildRequires:  go(github.com/renier/xmlrpc)
BuildRequires:  go(github.com/richardartoul/molecule)
BuildRequires:  go(github.com/rickar/props)
BuildRequires:  go(github.com/rivo/uniseg)
BuildRequires:  go(github.com/robfig/cron)
BuildRequires:  go(github.com/robfig/cron/v3)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/rs/cors)
BuildRequires:  go(github.com/rs/zerolog)
BuildRequires:  go(github.com/russross/blackfriday/v2)
BuildRequires:  go(github.com/rust-secure-code/go-rustaudit)
BuildRequires:  go(github.com/ryancurrah/gomodguard)
BuildRequires:  go(github.com/ryancurrah/gomodguard/v2)
BuildRequires:  go(github.com/ryanrolds/sqlclosecheck)
BuildRequires:  go(github.com/ryanuber/go-glob)
BuildRequires:  go(github.com/safchain/baloum)
BuildRequires:  go(github.com/safchain/ethtool)
BuildRequires:  go(github.com/sagikazarmark/locafero)
BuildRequires:  go(github.com/samber/lo)
BuildRequires:  go(github.com/samber/oops)
BuildRequires:  go(github.com/samuel/go-zookeeper)
BuildRequires:  go(github.com/sanposhiho/wastedassign/v2)
BuildRequires:  go(github.com/santhosh-tekuri/jsonschema/v5)
BuildRequires:  go(github.com/santhosh-tekuri/jsonschema/v6)
BuildRequires:  go(github.com/saracen/walker)
BuildRequires:  go(github.com/sasha-s/go-deadlock)
BuildRequires:  go(github.com/sashamelentyev/interfacebloat)
BuildRequires:  go(github.com/sashamelentyev/usestdlibvars)
BuildRequires:  go(github.com/sassoftware/go-rpmutils)
BuildRequires:  go(github.com/scaleway/scaleway-sdk-go)
BuildRequires:  go(github.com/secure-systems-lab/go-securesystemslib)
BuildRequires:  go(github.com/securego/gosec/v2)
BuildRequires:  go(github.com/segmentio/asm)
BuildRequires:  go(github.com/segmentio/encoding)
BuildRequires:  go(github.com/segmentio/fasthash)
BuildRequires:  go(github.com/sergi/go-diff)
BuildRequires:  go(github.com/sethvargo/go-limiter)
BuildRequires:  go(github.com/shirou/gopsutil/v3)
BuildRequires:  go(github.com/shirou/gopsutil/v4)
BuildRequires:  go(github.com/shirou/w32)
BuildRequires:  go(github.com/shoenig/go-m1cpu)
BuildRequires:  go(github.com/shogo82148/go-shuffle)
BuildRequires:  go(github.com/shopspring/decimal)
BuildRequires:  go(github.com/shurcooL/httpfs)
BuildRequires:  go(github.com/sijms/go-ora/v2)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/sivchari/containedctx)
BuildRequires:  go(github.com/skeema/knownhosts)
BuildRequires:  go(github.com/skydive-project/go-debouncer)
BuildRequires:  go(github.com/smartystreets/assertions)
BuildRequires:  go(github.com/smira/go-ftp-protocol)
BuildRequires:  go(github.com/smira/go-xz)
BuildRequires:  go(github.com/softlayer/softlayer-go)
BuildRequires:  go(github.com/sonatard/noctx)
BuildRequires:  go(github.com/sony/gobreaker)
BuildRequires:  go(github.com/sourcegraph/conc)
BuildRequires:  go(github.com/sourcegraph/go-diff)
BuildRequires:  go(github.com/spaolacci/murmur3)
BuildRequires:  go(github.com/spf13/afero)
BuildRequires:  go(github.com/spf13/cast)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/jwalterweatherman)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/spf13/viper)
BuildRequires:  go(github.com/ssgreg/nlreturn/v2)
BuildRequires:  go(github.com/stackitcloud/stackit-sdk-go/core)
BuildRequires:  go(github.com/stbenjam/no-sprintf-host-port)
BuildRequires:  go(github.com/stormcat24/protodep)
BuildRequires:  go(github.com/streadway/amqp)
BuildRequires:  go(github.com/stretchr/objx)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/subosito/gotenv)
BuildRequires:  go(github.com/swaggest/jsonschema-go)
BuildRequires:  go(github.com/swaggest/refl)
BuildRequires:  go(github.com/syndtr/gocapability)
BuildRequires:  go(github.com/tchap/go-patricia/v2)
BuildRequires:  go(github.com/tedsuo/ifrit)
BuildRequires:  go(github.com/tedsuo/rata)
BuildRequires:  go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common)
BuildRequires:  go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cvm)
BuildRequires:  go(github.com/tetafro/godot)
BuildRequires:  go(github.com/texttheater/golang-levenshtein)
BuildRequires:  go(github.com/tidwall/gjson)
BuildRequires:  go(github.com/tidwall/match)
BuildRequires:  go(github.com/tidwall/pretty)
BuildRequires:  go(github.com/tidwall/sjson)
BuildRequires:  go(github.com/tilinna/clock)
BuildRequires:  go(github.com/timakin/bodyclose)
BuildRequires:  go(github.com/timonwong/loggercheck)
BuildRequires:  go(github.com/tink-crypto/tink-go/v2)
BuildRequires:  go(github.com/tinylib/msgp)
BuildRequires:  go(github.com/tklauser/go-sysconf)
BuildRequires:  go(github.com/tklauser/numcpus)
BuildRequires:  go(github.com/tmthrgd/go-hex)
BuildRequires:  go(github.com/tomarrell/wrapcheck/v2)
BuildRequires:  go(github.com/tommy-muehle/go-mnd/v2)
BuildRequires:  go(github.com/trailofbits/go-mutexasserts)
BuildRequires:  go(github.com/tv42/httpunix)
BuildRequires:  go(github.com/twinj/uuid)
BuildRequires:  go(github.com/twitchtv/twirp)
BuildRequires:  go(github.com/twmb/franz-go)
BuildRequires:  go(github.com/twmb/franz-go/pkg/kadm)
BuildRequires:  go(github.com/twmb/franz-go/pkg/kmsg)
BuildRequires:  go(github.com/twmb/murmur3)
BuildRequires:  go(github.com/ua-parser/uap-go)
BuildRequires:  go(github.com/uber-go/gopatch)
BuildRequires:  go(github.com/uber/jaeger-client-go)
BuildRequires:  go(github.com/uber/jaeger-lib)
BuildRequires:  go(github.com/ugorji/go/codec)
BuildRequires:  go(github.com/ulikunitz/xz)
BuildRequires:  go(github.com/ultraware/funlen)
BuildRequires:  go(github.com/ultraware/whitespace)
BuildRequires:  go(github.com/uptrace/bun)
BuildRequires:  go(github.com/uptrace/bun/dialect/pgdialect)
BuildRequires:  go(github.com/uptrace/bun/driver/pgdriver)
BuildRequires:  go(github.com/urfave/cli/v2)
BuildRequires:  go(github.com/urfave/negroni)
BuildRequires:  go(github.com/uudashr/gocognit)
BuildRequires:  go(github.com/uudashr/iface)
BuildRequires:  go(github.com/valyala/fastjson)
BuildRequires:  go(github.com/vbatts/tar-split)
BuildRequires:  go(github.com/vektra/mockery/v3)
BuildRequires:  go(github.com/vibrantbyte/go-antpath)
BuildRequires:  go(github.com/vishvananda/netlink)
BuildRequires:  go(github.com/vishvananda/netns)
BuildRequires:  go(github.com/vito/go-sse)
BuildRequires:  go(github.com/vmihailenco/msgpack/v4)
BuildRequires:  go(github.com/vmihailenco/msgpack/v5)
BuildRequires:  go(github.com/vmihailenco/tagparser)
BuildRequires:  go(github.com/vmihailenco/tagparser/v2)
BuildRequires:  go(github.com/vmware/govmomi)
BuildRequires:  go(github.com/vultr/govultr/v3)
BuildRequires:  go(github.com/wI2L/jsondiff)
BuildRequires:  go(github.com/wadey/gocovmerge)
BuildRequires:  go(github.com/weppos/publicsuffix-go)
BuildRequires:  go(github.com/wk8/go-ordered-map/v2)
BuildRequires:  go(github.com/x448/float16)
BuildRequires:  go(github.com/xanzy/ssh-agent)
BuildRequires:  go(github.com/xdg-go/pbkdf2)
BuildRequires:  go(github.com/xdg-go/scram)
BuildRequires:  go(github.com/xdg-go/stringprep)
BuildRequires:  go(github.com/xeipuuv/gojsonpointer)
BuildRequires:  go(github.com/xeipuuv/gojsonreference)
BuildRequires:  go(github.com/xeipuuv/gojsonschema)
BuildRequires:  go(github.com/xen0n/gosmopolitan)
BuildRequires:  go(github.com/xi2/xz)
BuildRequires:  go(github.com/xlab/treeprint)
BuildRequires:  go(github.com/xo/terminfo)
BuildRequires:  go(github.com/xor-gate/ar)
BuildRequires:  go(github.com/xrash/smetrics)
BuildRequires:  go(github.com/yagipy/maintidx)
BuildRequires:  go(github.com/yashtewari/glob-intersection)
BuildRequires:  go(github.com/yeya24/promlinter)
BuildRequires:  go(github.com/ykadowak/zerologlint)
BuildRequires:  go(github.com/yosida95/uritemplate/v3)
BuildRequires:  go(github.com/youmark/pkcs8)
BuildRequires:  go(github.com/yusufpapurcu/wmi)
BuildRequires:  go(github.com/zclconf/go-cty)
BuildRequires:  go(github.com/zeebo/xxh3)
BuildRequires:  go(github.com/zorkian/go-datadog-api)
BuildRequires:  go(gitlab.com/bosi/decorder)
BuildRequires:  go(gitlab.com/gitlab-org/api/client-go)
BuildRequires:  go(go-simpler.org/musttag)
BuildRequires:  go(go-simpler.org/sloglint)
BuildRequires:  go(go.augendre.info/arangolint)
BuildRequires:  go(go.augendre.info/fatcontext)
BuildRequires:  go(go.etcd.io/bbolt)
BuildRequires:  go(go.etcd.io/etcd/api/v3)
BuildRequires:  go(go.etcd.io/etcd/client/pkg/v3)
BuildRequires:  go(go.etcd.io/etcd/client/v2)
BuildRequires:  go(go.etcd.io/etcd/client/v3)
BuildRequires:  go(go.mongodb.org/mongo-driver)
BuildRequires:  go(go.mongodb.org/mongo-driver/v2)
BuildRequires:  go(go.opencensus.io)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/collector)
BuildRequires:  go(go.opentelemetry.io/collector/client)
BuildRequires:  go(go.opentelemetry.io/collector/component)
BuildRequires:  go(go.opentelemetry.io/collector/component/componentstatus)
BuildRequires:  go(go.opentelemetry.io/collector/component/componenttest)
BuildRequires:  go(go.opentelemetry.io/collector/config/configauth)
BuildRequires:  go(go.opentelemetry.io/collector/config/configcompression)
BuildRequires:  go(go.opentelemetry.io/collector/config/configgrpc)
BuildRequires:  go(go.opentelemetry.io/collector/config/confighttp)
BuildRequires:  go(go.opentelemetry.io/collector/config/configmiddleware)
BuildRequires:  go(go.opentelemetry.io/collector/config/confignet)
BuildRequires:  go(go.opentelemetry.io/collector/config/configopaque)
BuildRequires:  go(go.opentelemetry.io/collector/config/configoptional)
BuildRequires:  go(go.opentelemetry.io/collector/config/configretry)
BuildRequires:  go(go.opentelemetry.io/collector/config/configtelemetry)
BuildRequires:  go(go.opentelemetry.io/collector/config/configtls)
BuildRequires:  go(go.opentelemetry.io/collector/confmap)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/provider/envprovider)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/provider/fileprovider)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/provider/httpprovider)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/provider/httpsprovider)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/provider/yamlprovider)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/xconfmap)
BuildRequires:  go(go.opentelemetry.io/collector/connector)
BuildRequires:  go(go.opentelemetry.io/collector/connector/connectortest)
BuildRequires:  go(go.opentelemetry.io/collector/connector/xconnector)
BuildRequires:  go(go.opentelemetry.io/collector/consumer)
BuildRequires:  go(go.opentelemetry.io/collector/consumer/consumererror)
BuildRequires:  go(go.opentelemetry.io/collector/consumer/consumererror/xconsumererror)
BuildRequires:  go(go.opentelemetry.io/collector/consumer/consumertest)
BuildRequires:  go(go.opentelemetry.io/collector/consumer/xconsumer)
BuildRequires:  go(go.opentelemetry.io/collector/exporter)
BuildRequires:  go(go.opentelemetry.io/collector/exporter/debugexporter)
BuildRequires:  go(go.opentelemetry.io/collector/exporter/exporterhelper)
BuildRequires:  go(go.opentelemetry.io/collector/exporter/exporterhelper/xexporterhelper)
BuildRequires:  go(go.opentelemetry.io/collector/exporter/exportertest)
BuildRequires:  go(go.opentelemetry.io/collector/exporter/nopexporter)
BuildRequires:  go(go.opentelemetry.io/collector/exporter/otlpexporter)
BuildRequires:  go(go.opentelemetry.io/collector/exporter/otlphttpexporter)
BuildRequires:  go(go.opentelemetry.io/collector/exporter/xexporter)
BuildRequires:  go(go.opentelemetry.io/collector/extension)
BuildRequires:  go(go.opentelemetry.io/collector/extension/extensionauth)
BuildRequires:  go(go.opentelemetry.io/collector/extension/extensioncapabilities)
BuildRequires:  go(go.opentelemetry.io/collector/extension/extensionmiddleware)
BuildRequires:  go(go.opentelemetry.io/collector/extension/extensiontest)
BuildRequires:  go(go.opentelemetry.io/collector/extension/xextension)
BuildRequires:  go(go.opentelemetry.io/collector/extension/zpagesextension)
BuildRequires:  go(go.opentelemetry.io/collector/featuregate)
BuildRequires:  go(go.opentelemetry.io/collector/filter)
BuildRequires:  go(go.opentelemetry.io/collector/internal/componentalias)
BuildRequires:  go(go.opentelemetry.io/collector/internal/fanoutconsumer)
BuildRequires:  go(go.opentelemetry.io/collector/internal/memorylimiter)
BuildRequires:  go(go.opentelemetry.io/collector/internal/sharedcomponent)
BuildRequires:  go(go.opentelemetry.io/collector/internal/telemetry)
BuildRequires:  go(go.opentelemetry.io/collector/otelcol)
BuildRequires:  go(go.opentelemetry.io/collector/otelcol/otelcoltest)
BuildRequires:  go(go.opentelemetry.io/collector/pdata)
BuildRequires:  go(go.opentelemetry.io/collector/pdata/pprofile)
BuildRequires:  go(go.opentelemetry.io/collector/pdata/testdata)
BuildRequires:  go(go.opentelemetry.io/collector/pdata/xpdata)
BuildRequires:  go(go.opentelemetry.io/collector/pipeline)
BuildRequires:  go(go.opentelemetry.io/collector/pipeline/xpipeline)
BuildRequires:  go(go.opentelemetry.io/collector/processor)
BuildRequires:  go(go.opentelemetry.io/collector/processor/batchprocessor)
BuildRequires:  go(go.opentelemetry.io/collector/processor/memorylimiterprocessor)
BuildRequires:  go(go.opentelemetry.io/collector/processor/processorhelper)
BuildRequires:  go(go.opentelemetry.io/collector/processor/processorhelper/xprocessorhelper)
BuildRequires:  go(go.opentelemetry.io/collector/processor/processortest)
BuildRequires:  go(go.opentelemetry.io/collector/processor/xprocessor)
BuildRequires:  go(go.opentelemetry.io/collector/receiver)
BuildRequires:  go(go.opentelemetry.io/collector/receiver/nopreceiver)
BuildRequires:  go(go.opentelemetry.io/collector/receiver/otlpreceiver)
BuildRequires:  go(go.opentelemetry.io/collector/receiver/receiverhelper)
BuildRequires:  go(go.opentelemetry.io/collector/receiver/receivertest)
BuildRequires:  go(go.opentelemetry.io/collector/receiver/xreceiver)
BuildRequires:  go(go.opentelemetry.io/collector/scraper)
BuildRequires:  go(go.opentelemetry.io/collector/scraper/scraperhelper)
BuildRequires:  go(go.opentelemetry.io/collector/semconv)
BuildRequires:  go(go.opentelemetry.io/collector/service)
BuildRequires:  go(go.opentelemetry.io/collector/service/hostcapabilities)
BuildRequires:  go(go.opentelemetry.io/contrib/bridges/otelzap)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/httptrace/otelhttptrace)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/runtime)
BuildRequires:  go(go.opentelemetry.io/contrib/otelconf)
BuildRequires:  go(go.opentelemetry.io/contrib/propagators/b3)
BuildRequires:  go(go.opentelemetry.io/contrib/zpages)
BuildRequires:  go(go.opentelemetry.io/ebpf-profiler)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploggrpc)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploghttp)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetricgrpc)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlptrace)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/prometheus)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/stdout/stdoutlog)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/stdout/stdoutmetric)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/stdout/stdouttrace)
BuildRequires:  go(go.opentelemetry.io/otel/log)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/log)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/metric)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.opentelemetry.io/proto/otlp)
BuildRequires:  go(go.temporal.io/api)
BuildRequires:  go(go.temporal.io/sdk)
BuildRequires:  go(go.uber.org/atomic)
BuildRequires:  go(go.uber.org/automaxprocs)
BuildRequires:  go(go.uber.org/dig)
BuildRequires:  go(go.uber.org/fx)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.uber.org/zap/exp)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(go.yaml.in/yaml/v4)
BuildRequires:  go(go4.org/intern)
BuildRequires:  go(go4.org/mem)
BuildRequires:  go(go4.org/netipx)
BuildRequires:  go(go4.org/unsafe/assume-no-moving-gc)
BuildRequires:  go(golang.org/x/arch)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/exp/typeparams)
BuildRequires:  go(golang.org/x/lint)
BuildRequires:  go(golang.org/x/mobile)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/perf)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/telemetry)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/xerrors)
BuildRequires:  go(gomodules.xyz/jsonpatch/v2)
BuildRequires:  go(gonum.org/v1/gonum)
BuildRequires:  go(google.golang.org/api)
BuildRequires:  go(google.golang.org/appengine)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/grpc/cmd/protoc-gen-go-grpc)
BuildRequires:  go(google.golang.org/grpc/examples)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/DataDog/dd-trace-go.v1)
BuildRequires:  go(gopkg.in/Knetic/govaluate.v3)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/cheggaaa/pb.v1)
BuildRequires:  go(gopkg.in/evanphx/json-patch.v4)
BuildRequires:  go(gopkg.in/inf.v0)
BuildRequires:  go(gopkg.in/ini.v1)
BuildRequires:  go(gopkg.in/natefinch/lumberjack.v2)
BuildRequires:  go(gopkg.in/neurosnap/sentences.v1)
BuildRequires:  go(gopkg.in/tomb.v1)
BuildRequires:  go(gopkg.in/warnings.v0)
BuildRequires:  go(gopkg.in/yaml.v2)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(gopkg.in/zorkian/go-datadog-api.v2)
BuildRequires:  go(gotest.tools/gotestsum)
BuildRequires:  go(gotest.tools/v3)
BuildRequires:  go(honnef.co/go/tools)
BuildRequires:  go(istio.io/api)
BuildRequires:  go(istio.io/client-go)
BuildRequires:  go(k8s.io/api)
BuildRequires:  go(k8s.io/apiextensions-apiserver)
BuildRequires:  go(k8s.io/apimachinery)
BuildRequires:  go(k8s.io/apiserver)
BuildRequires:  go(k8s.io/autoscaler/vertical-pod-autoscaler)
BuildRequires:  go(k8s.io/cli-runtime)
BuildRequires:  go(k8s.io/client-go)
BuildRequires:  go(k8s.io/cloud-provider)
BuildRequires:  go(k8s.io/component-base)
BuildRequires:  go(k8s.io/component-helpers)
BuildRequires:  go(k8s.io/cri-api)
BuildRequires:  go(k8s.io/cri-client)
BuildRequires:  go(k8s.io/csi-translation-lib)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/kms)
BuildRequires:  go(k8s.io/kube-aggregator)
BuildRequires:  go(k8s.io/kube-openapi)
BuildRequires:  go(k8s.io/kube-state-metrics/v2)
BuildRequires:  go(k8s.io/kubectl)
BuildRequires:  go(k8s.io/kubelet)
BuildRequires:  go(k8s.io/metrics)
BuildRequires:  go(k8s.io/sample-controller)
BuildRequires:  go(k8s.io/utils)
BuildRequires:  go(lukechampine.com/frand)
BuildRequires:  go(mellium.im/sasl)
BuildRequires:  go(modernc.org/sqlite)
BuildRequires:  go(mvdan.cc/gofumpt)
BuildRequires:  go(mvdan.cc/sh/v3)
BuildRequires:  go(mvdan.cc/unparam)
BuildRequires:  go(pgregory.net/rapid)
BuildRequires:  go(sigs.k8s.io/apiserver-network-proxy/konnectivity-client)
BuildRequires:  go(sigs.k8s.io/controller-runtime)
BuildRequires:  go(sigs.k8s.io/custom-metrics-apiserver)
BuildRequires:  go(sigs.k8s.io/gateway-api)
BuildRequires:  go(sigs.k8s.io/json)
BuildRequires:  go(sigs.k8s.io/karpenter)
BuildRequires:  go(sigs.k8s.io/kustomize/api)
BuildRequires:  go(sigs.k8s.io/kustomize/kyaml)
BuildRequires:  go(sigs.k8s.io/randfill)
BuildRequires:  go(sigs.k8s.io/structured-merge-diff/v6)
BuildRequires:  go(sigs.k8s.io/yaml)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/DataDog/datadog-agent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/bazel/rules/cws_codegen) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/bazel/rules/go_build_tags) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/bazel/rules/go_stringer) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/bazel/rules/write_pb_go) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/command) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/common/misconfig) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/common/signals) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/analyzelogs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/check) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/configcheck) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/controlsvc) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/coverage) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/createschema) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/diagnose) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/dogstatsd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/dogstatsdcapture) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/dogstatsdreplay) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/dogstatsdstats) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/experimental) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/flare) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/health) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/hostname) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/import) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/integrations) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/jmx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/launchgui) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/otel) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/processchecks) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/remoteconfig) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/run) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/run/internal/clcrunnerapi) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/run/internal/clcrunnerapi/v1) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/run/internal/settings) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/secret) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/secrethelper) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/snmp) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/status) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/stop) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/streamep) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/streamlogs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/taggerlist) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/validatepodannotation) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/version) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/workloadfilterlist) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/subcommands/workloadlist) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/windows/controlsvc) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/agent/windows/service) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent-cloudfoundry/command) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent-cloudfoundry/subcommands) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent-cloudfoundry/subcommands/run) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent-cloudfoundry/subcommands/version) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/admission) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/api) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/api/agent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/api/v1) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/api/v1/languagedetection) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/api/v2/series) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/command) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/custommetrics) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/subcommands) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/subcommands/autoscalerlist) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/subcommands/check) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/subcommands/clusterchecks) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/subcommands/compliance) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/subcommands/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/subcommands/configcheck) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/subcommands/coverage) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/subcommands/diagnose) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/subcommands/flare) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/subcommands/health) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/subcommands/metamap) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/subcommands/secrethelper) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/subcommands/start) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/subcommands/status) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/subcommands/taggerlist) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/subcommands/telemetry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/subcommands/version) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cluster-agent/subcommands/workloadlist) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cws-instrumentation/command) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cws-instrumentation/flags) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cws-instrumentation/subcommands) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cws-instrumentation/subcommands/healthcmd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cws-instrumentation/subcommands/injectcmd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cws-instrumentation/subcommands/selftestscmd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cws-instrumentation/subcommands/setupcmd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/cws-instrumentation/subcommands/tracecmd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/dogstatsd/command) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/dogstatsd/subcommands/start) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/host-profiler/command) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/host-profiler/globalparams) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/host-profiler/subcommands/run) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/installer/command) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/installer/subcommands) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/installer/subcommands/daemon) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/installer/user) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/internal/runcmd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/iot-agent/subcommands) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/otel-agent/command) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/otel-agent/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/otel-agent/subcommands) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/otel-agent/subcommands/controlsvc) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/otel-agent/subcommands/coverage) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/otel-agent/subcommands/flare) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/otel-agent/subcommands/run) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/otel-agent/subcommands/status) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/otel-agent/windows/controlsvc) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/privateactionrunner/command) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/privateactionrunner/subcommands) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/privateactionrunner/subcommands/run) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/privateactionrunner/subcommands/version) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/process-agent/api) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/process-agent/command) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/process-agent/flags) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/process-agent/subcommands) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/process-agent/subcommands/check) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/process-agent/subcommands/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/process-agent/subcommands/coverage) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/process-agent/subcommands/status) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/process-agent/subcommands/taggerlist) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/process-agent/subcommands/version) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/process-agent/subcommands/workloadlist) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/secret-generic-connector/backend) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/secret-generic-connector/backend/akeyless) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/secret-generic-connector/backend/aws) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/secret-generic-connector/backend/azure) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/secret-generic-connector/backend/docker) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/secret-generic-connector/backend/file) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/secret-generic-connector/backend/gcp) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/secret-generic-connector/backend/hashicorp) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/secret-generic-connector/backend/kubernetes) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/secret-generic-connector/internal/tools) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/secret-generic-connector/secret) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/secrethelper) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/secrethelper/providers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/security-agent/api) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/security-agent/api/agent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/security-agent/command) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/security-agent/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/security-agent/subcommands) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/security-agent/subcommands/compliance) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/security-agent/subcommands/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/security-agent/subcommands/coverage) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/security-agent/subcommands/flare) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/security-agent/subcommands/start) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/security-agent/subcommands/status) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/security-agent/subcommands/version) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/security-agent/subcommands/workloadlist) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/serverless-init/cloudservice) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/serverless-init/enhanced-metrics) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/serverless-init/exitcode) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/serverless-init/log) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/serverless-init/mode) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/serverless-init/tag) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/serverless-init/trace) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/system-probe/api) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/system-probe/api/debug) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/system-probe/command) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/system-probe/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/system-probe/modules) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/system-probe/subcommands) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/system-probe/subcommands/compliance) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/system-probe/subcommands/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/system-probe/subcommands/coverage) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/system-probe/subcommands/debug) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/system-probe/subcommands/ebpf) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/system-probe/subcommands/modrestart) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/system-probe/subcommands/run) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/system-probe/subcommands/runtime) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/system-probe/subcommands/usm) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/system-probe/subcommands/version) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/system-probe/windows/service) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/systray/command) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/trace-agent/command) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/trace-agent/config/remote) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/trace-agent/internal/flags) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/trace-agent/subcommands) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/trace-agent/subcommands/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/trace-agent/subcommands/controlsvc) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/trace-agent/subcommands/coverage) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/trace-agent/subcommands/info) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/trace-agent/subcommands/run) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/trace-agent/test) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/cmd/trace-agent/windows/controlsvc) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/agent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/agent/autoexit/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/agent/autoexit/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/agent/autoexit/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/agent/autoexit/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/agent/cloudfoundrycontainer/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/agent/cloudfoundrycontainer/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/agent/cloudfoundrycontainer/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/agent/cloudfoundrycontainer/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/agent/expvarserver/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/agent/expvarserver/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/agent/expvarserver/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/agent/expvarserver/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/agent/jmxlogger) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/agent/jmxlogger/jmxloggerimpl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/aggregator) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/aggregator/demultiplexer) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/aggregator/demultiplexer/demultiplexerimpl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/aggregator/demultiplexerendpoint/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/aggregator/demultiplexerendpoint/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/aggregator/demultiplexerendpoint/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/anomalydetection/hfrunner/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/anomalydetection/hfrunner/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/anomalydetection/hfrunner/fx-noop) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/anomalydetection/hfrunner/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/anomalydetection/hfrunner/impl-noop) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/anomalydetection/logssource/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/anomalydetection/logssource/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/anomalydetection/logssource/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/anomalydetection/observer/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/anomalydetection/observer/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/anomalydetection/observer/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/anomalydetection/observer/impl/patterns) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/anomalydetection/recorder/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/anomalydetection/recorder/fx-noop) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/anomalydetection/recorder/impl-noop) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/anomalydetection/reporter/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/anomalydetection/reporter/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/anomalydetection/reporter/fx-noop) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/anomalydetection/reporter/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/anomalydetection/reporter/impl-noop) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/anomalydetection/reporter/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/api) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/api/api/apiimpl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/api/api/apiimpl/internal/agent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/api/api/apiimpl/internal/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/api/api/apiimpl/listener) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/api/api/apiimpl/observability) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/api/api/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/api/api/utils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/api/api/utils/stream) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/api/commonendpoints/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/api/commonendpoints/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/api/grpcserver/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/api/grpcserver/fx-agent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/api/grpcserver/fx-none) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/api/grpcserver/helpers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/api/grpcserver/impl-agent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/api/grpcserver/impl-none) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/api/grpcserver/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/autoscaling/datadogclient/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/autoscaling/datadogclient/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/autoscaling/datadogclient/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/autoscaling/datadogclient/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/checks) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/checks/agentcrashdetect/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/checks/agentcrashdetect/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/checks/agentcrashdetect/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/checks/agentcrashdetect/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/checks/windowseventlog/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/checks/windowseventlog/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/checks/windowseventlog/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/checks/windowseventlog/impl/check) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/checks/windowseventlog/impl/check/eventdatafilter) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/checks/windowseventlog/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/checks/winregistry/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/checks/winregistry/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/checks/winregistry/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/checks/winregistry/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/collector) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/collector/collector) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/collector/collector/collectorimpl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/collector/collector/collectorimpl/internal/middleware) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/connectivitychecker/checker) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/connectivitychecker/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/connectivitychecker/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/connectivitychecker/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/agenttelemetry/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/agenttelemetry/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/agenttelemetry/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/autodiscovery) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/autodiscovery/autodiscoveryimpl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/autodiscovery/common/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/autodiscovery/common/utils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/autodiscovery/configresolver) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/autodiscovery/integration) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/autodiscovery/listeners) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/autodiscovery/noopimpl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/autodiscovery/proto) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/autodiscovery/providers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/autodiscovery/providers/datastreams) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/autodiscovery/providers/names) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/autodiscovery/providers/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/autodiscovery/scheduler) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/autodiscovery/status) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/autodiscovery/stream) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/autodiscovery/telemetry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/configstream/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/configstream/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/configstream/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/configstream/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/configstream/server) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/configstreamconsumer/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/configstreamconsumer/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/configstreamconsumer/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/configstreamconsumer/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/configsync) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/configsync/configsyncimpl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/delegatedauth) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/delegatedauth/api) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/delegatedauth/api/cloudauth/aws) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/delegatedauth/api/cloudauth/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/delegatedauth/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/delegatedauth/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/delegatedauth/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/delegatedauth/fx-noop) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/delegatedauth/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/delegatedauth/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/delegatedauth/noop-impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/delegatedauth/noop-impl/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/diagnose/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/diagnose/format) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/diagnose/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/diagnose/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/diagnose/local) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/diagnose/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/flare) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/flare/builder) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/flare/flareimpl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/flare/helpers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/flare/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/fxinstrumentation/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/fxinstrumentation/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/fxinstrumentation/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/gui) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/gui/guiimpl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/healthprobe/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/healthprobe/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/healthprobe/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/hostname) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/hostname/hostnameimpl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/hostname/hostnameinterface) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/hostname/remotehostnameimpl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/ipc/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/ipc/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/ipc/fx-none) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/ipc/httphelpers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/ipc/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/ipc/impl-none) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/ipc/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/log/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/log/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/log/fx-systemprobe) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/log/fx-trace) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/log/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/log/impl-systemprobe) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/log/impl-trace) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/log/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/lsof/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/lsof/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/lsof/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/lsof/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/pid/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/pid/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/pid/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/pid/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/profiler/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/profiler/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/profiler/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/profiler/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/remoteagent/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/remoteagent/fx-process) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/remoteagent/fx-securityagent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/remoteagent/fx-systemprobe) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/remoteagent/fx-template) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/remoteagent/fx-trace) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/remoteagent/helper) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/remoteagent/impl-process) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/remoteagent/impl-securityagent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/remoteagent/impl-systemprobe) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/remoteagent/impl-template) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/remoteagent/impl-trace) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/remoteagentregistry/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/remoteagentregistry/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/remoteagentregistry/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/remoteagentregistry/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/remoteagentregistry/status) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/remoteagentregistry/util) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/remoteflags/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/remoteflags/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/remoteflags/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/remoteflags/impl-noop) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/remoteflags/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/secrets/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/secrets/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/secrets/fx-noop) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/secrets/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/secrets/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/secrets/noop-impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/secrets/noop-impl/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/secrets/utils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/settings) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/settings/settingsimpl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/status) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/status/statusimpl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/sysprobeconfig/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/sysprobeconfig/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/sysprobeconfig/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/sysprobeconfig/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/api) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/collectors) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/fx-dual) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/fx-mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/fx-noop) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/fx-optional-remote) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/fx-remote) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/generic_store) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/impl-dual) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/impl-noop) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/impl-optional-remote) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/impl-remote) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/k8s_metadata) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/kubetags) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/origindetection) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/proto) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/server) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/subscriber) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/taglist) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/tags) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/tagstore) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/telemetry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/tagger/utils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/telemetry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/telemetry/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/telemetry/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/telemetry/fx-noop) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/telemetry/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/telemetry/impl/noops) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/telemetry/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadfilter/baseimpl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadfilter/catalog) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadfilter/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadfilter/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadfilter/fx-mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadfilter/fx-remote) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadfilter/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadfilter/impl/parse) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadfilter/legacy) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadfilter/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadfilter/program) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadfilter/proto) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadfilter/remoteimpl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadfilter/server) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadfilter/telemetry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadfilter/util/celprogram) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadfilter/util/docker) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadfilter/util/workloadmeta) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/catalog) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/catalog-clusteragent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/catalog-core) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/catalog-dogstatsd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/catalog-otel) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/catalog-remote) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/internal/cloudfoundry/container) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/internal/cloudfoundry/vm) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/internal/containerd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/internal/crio) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/internal/docker) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/internal/ecs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/internal/kubeapiserver) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/internal/kubelet) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/internal/kubemetadata) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/internal/nvml) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/internal/podman) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/internal/process) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/internal/remote) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/internal/remote/processcollector) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/internal/remote/sbomcollector) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/internal/remote/workloadmeta) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/sbomutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/util) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/collectors/util/kubernetes_resource_parsers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/defaults) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/fx-mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/init) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/proto) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/server) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/core/workloadmeta/telemetry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dataobs/queryactions/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dataobs/queryactions/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dataobs/queryactions/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/constants) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/http/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/http/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/http/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/http/impl/internal/reader) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/listeners) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/listeners/ratelimit) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/mapper) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/packets) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/pidmap/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/pidmap/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/pidmap/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/replay/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/replay/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/replay/fx-mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/replay/fx-noop) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/replay/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/replay/impl-noop) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/replay/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/server/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/server/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/server/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/server/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/serverDebug/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/serverDebug/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/serverDebug/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/serverDebug/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/statsd/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/statsd/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/statsd/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/statsd/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/statsd/otel) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/status/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/status/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/dogstatsd/status/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/etw/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/etw/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/etw/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/filterlist/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/filterlist/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/filterlist/fx-mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/filterlist/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/fleetstatus/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/fleetstatus/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/fleetstatus/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/forwarder) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/forwarder/connectionsforwarder/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/forwarder/connectionsforwarder/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/forwarder/connectionsforwarder/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/forwarder/connectionsforwarder/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/forwarder/defaultforwarder) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/forwarder/defaultforwarder/endpoints) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/forwarder/defaultforwarder/internal/retry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/forwarder/defaultforwarder/resolver) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/forwarder/defaultforwarder/transaction) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/forwarder/eventplatform) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/forwarder/eventplatform/eventplatformimpl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/forwarder/eventplatformreceiver) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/forwarder/eventplatformreceiver/eventplatformreceiverimpl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/forwarder/orchestrator) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/forwarder/orchestrator/orchestratorimpl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/forwarder/orchestrator/orchestratorinterface) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/haagent/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/haagent/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/haagent/helpers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/haagent/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/haagent/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/healthplatform) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/healthplatform/forwarder/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/healthplatform/forwarder/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/healthplatform/forwarder/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/healthplatform/forwarder/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/healthplatform/fx-noop) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/healthplatform/issues) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/healthplatform/issues/admisconfig) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/healthplatform/issues/admissionprobe) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/healthplatform/issues/checkfailure) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/healthplatform/issues/dockerpermissions) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/healthplatform/issues/rofspermissions) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/healthplatform/noop-impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/healthplatform/scheduler/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/healthplatform/scheduler/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/healthplatform/scheduler/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/healthplatform/scheduler/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/healthplatform/store/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/healthplatform/store/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/healthplatform/store/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/healthplatform/store/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/healthplatform/store/noop-impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/host-profiler) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/host-profiler/collector/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/host-profiler/collector/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/host-profiler/collector/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/host-profiler/collector/impl/agentprovider) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/host-profiler/collector/impl/converters) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/host-profiler/collector/impl/extensions/hpflareextension) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/host-profiler/collector/impl/params) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/host-profiler/collector/impl/processor/ddhostnameprocessor) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/host-profiler/collector/impl/receiver) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/host-profiler/flare/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/host-profiler/flare/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/host-profiler/oom) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/host-profiler/symboluploader) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/host-profiler/symboluploader/cgroup) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/host-profiler/symboluploader/pclntab) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/host-profiler/symboluploader/pipeline) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/host-profiler/symboluploader/symbol) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/host-profiler/symboluploader/symbolcopier) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/host-profiler/version) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/languagedetection/client/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/languagedetection/client/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/languagedetection/client/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/languagedetection/client/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logonduration/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logonduration/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logonduration/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs-library) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs-library/client) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs-library/client/http) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs-library/client/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs-library/client/tcp) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs-library/kubehealth/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs-library/kubehealth/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs-library/kubehealth/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs-library/kubehealth/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs-library/metrics) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs-library/pipeline) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs-library/pipeline/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs-library/processor) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs-library/sender) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs-library/sender/http) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs-library/sender/tcp) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs-library/utils/ipfilter) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs-library/utils/tls) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs-library/utils/tls/certreloader) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs/adscheduler/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs/adscheduler/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs/adscheduler/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs/agent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs/agent/agentimpl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs/agent/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs/agent/flare) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs/auditor/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs/auditor/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs/auditor/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs/auditor/impl-none) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs/auditor/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs/integrations/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs/integrations/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs/integrations/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs/streamlogs/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs/streamlogs/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs/streamlogs/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/logs/streamlogs/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/clusteragent/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/clusteragent/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/clusteragent/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/clusterchecks/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/clusterchecks/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/clusterchecks/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/haagent/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/haagent/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/haagent/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/host/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/host/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/host/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/host/impl/hosttags) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/host/impl/utils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/host/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/hostgpu/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/hostgpu/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/hostgpu/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/hostsysteminfo/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/hostsysteminfo/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/hostsysteminfo/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/internal/util) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/inventoryagent/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/inventoryagent/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/inventoryagent/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/inventoryagent/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/inventorychecks/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/inventorychecks/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/inventorychecks/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/inventorychecks/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/inventoryhost/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/inventoryhost/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/inventoryhost/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/inventoryhost/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/packagesigning/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/packagesigning/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/packagesigning/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/packagesigning/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/packagesigning/utils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/resources/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/resources/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/resources/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/resources/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/runner/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/runner/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/runner/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/securityagent/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/securityagent/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/securityagent/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/systemprobe/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/systemprobe/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/metadata/systemprobe/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/ndmtmp) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/ndmtmp/forwarder/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/ndmtmp/forwarder/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/ndmtmp/forwarder/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/ndmtmp/forwarder/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/netflow) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/netflow/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/netflow/config/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/netflow/config/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/netflow/config/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/netflow/config/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/netflow/flowaggregator) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/netflow/format) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/netflow/goflowlib) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/netflow/goflowlib/additionalfields) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/netflow/goflowlib/netflowstate) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/netflow/payload) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/netflow/portrollup) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/netflow/server/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/netflow/server/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/netflow/server/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/netflow/testutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/netflow/topn) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/networkconfigmanagement/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/networkconfigmanagement/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/networkconfigmanagement/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/networkconfigmanagement/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/networkpath) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/networkpath/npcollector/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/networkpath/npcollector/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/networkpath/npcollector/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/networkpath/npcollector/impl/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/networkpath/npcollector/impl/connfilter) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/networkpath/npcollector/impl/pathteststore) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/networkpath/npcollector/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/networkpath/npcollector/model) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/networkpath/traceroute/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/networkpath/traceroute/fx-local) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/networkpath/traceroute/fx-remote) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/networkpath/traceroute/impl-local) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/networkpath/traceroute/impl-remote) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/networkpath/traceroute/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/notableevents/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/notableevents/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/notableevents/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/offlinereporter/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/offlinereporter/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/offlinereporter/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/offlinereporter/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/collector-contrib/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/collector-contrib/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/collector-contrib/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/collector/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/collector/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/collector/fx-pipeline) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/collector/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/collector/impl-pipeline) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/converter/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/converter/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/converter/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/ddflareextension/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/ddflareextension/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/ddflareextension/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/ddflareextension/impl/internal/metadata) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/ddflareextension/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/ddprofilingextension/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/ddprofilingextension/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/ddprofilingextension/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/dogtelextension/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/dogtelextension/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/dogtelextension/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/dogtelextension/impl/metadata) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/dogtelextension/impl/metrics) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/logsagentpipeline) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/logsagentpipeline/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/logsagentpipeline/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/logsagentpipeline/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/logsagentpipeline/logsagentpipelineimpl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/otlp) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/otlp/components/exporter/datadogexporter) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/otlp/components/exporter/logsagentexporter) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/otlp/components/exporter/serializerexporter) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/otlp/components/metricsclient) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/otlp/components/processor/infraattributesprocessor) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/otlp/configcheck) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/otlp/datatype) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/otlp/integrationtest) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/otlp/internal/configutils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/otlp/testutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/status/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/status/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/otelcol/status/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/privateactionrunner/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/privateactionrunner/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/privateactionrunner/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/privateactionrunner/status/statusimpl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/agent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/agent/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/agent/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/agent/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/apiserver) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/connectionscheck/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/connectionscheck/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/connectionscheck/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/containercheck/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/containercheck/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/containercheck/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/containercheck/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/expvars/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/expvars/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/expvars/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/forwarders/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/forwarders/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/forwarders/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/forwarders/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/gpusubscriber/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/gpusubscriber/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/gpusubscriber/fx-mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/gpusubscriber/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/gpusubscriber/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/hostinfo/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/hostinfo/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/hostinfo/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/hostinfo/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/processcheck/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/processcheck/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/processcheck/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/processdiscoverycheck/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/processdiscoverycheck/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/processdiscoverycheck/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/profiler/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/profiler/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/profiler/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/rtcontainercheck/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/rtcontainercheck/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/rtcontainercheck/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/runner/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/runner/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/runner/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/status/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/status/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/status/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/submitter/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/submitter/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/submitter/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/submitter/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/process/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/publishermetadatacache/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/publishermetadatacache/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/publishermetadatacache/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/rdnsquerier/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/rdnsquerier/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/rdnsquerier/fx-mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/rdnsquerier/fx-none) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/rdnsquerier/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/rdnsquerier/impl-none) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/rdnsquerier/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/remote-config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/remote-config/rcclient/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/remote-config/rcclient/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/remote-config/rcclient/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/remote-config/rcclient/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/remote-config/rcprotocoltest/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/remote-config/rcprotocoltest/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/remote-config/rcprotocoltest/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/remote-config/rcservice/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/remote-config/rcservice/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/remote-config/rcservice/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/remote-config/rcservicemrf/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/remote-config/rcservicemrf/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/remote-config/rcservicemrf/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/remote-config/rcstatus/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/remote-config/rcstatus/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/remote-config/rcstatus/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/remote-config/rctelemetryreporter/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/remote-config/rctelemetryreporter/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/remote-config/rctelemetryreporter/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/serializer/logscompression) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/serializer/logscompression/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/serializer/logscompression/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/serializer/logscompression/fx-mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/serializer/logscompression/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/serializer/metricscompression) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/serializer/metricscompression/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/serializer/metricscompression/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/serializer/metricscompression/fx-mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/serializer/metricscompression/fx-otel) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/serializer/metricscompression/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmpscan/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmpscan/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmpscan/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmpscan/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmpscanmanager/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmpscanmanager/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmpscanmanager/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmpscanmanager/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/config/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/config/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/config/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/formatter/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/formatter/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/formatter/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/forwarder/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/forwarder/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/forwarder/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/listener/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/listener/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/listener/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/oidresolver/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/oidresolver/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/oidresolver/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/packet) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/senderhelper) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/server/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/server/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/server/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/snmplog) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/status/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/status/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/snmptraps/status/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/softwareinventory/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/softwareinventory/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/softwareinventory/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/syntheticstestscheduler/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/syntheticstestscheduler/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/syntheticstestscheduler/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/syntheticstestscheduler/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/systray) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/systray/systray/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/systray/systray/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/systray/systray/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/systray/systray/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace-telemetry/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace-telemetry/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace-telemetry/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace/agent/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace/agent/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace/agent/fx-mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace/agent/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace/compression/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace/compression/fx-gzip) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace/compression/fx-zstd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace/compression/impl-gzip) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace/compression/impl-zstd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace/config/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace/config/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace/config/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace/config/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace/etwtracer/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace/etwtracer/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace/etwtracer/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace/payload-modifier/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace/payload-modifier/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace/payload-modifier/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace/status/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace/status/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/trace/status/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/updater) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/updater/daemonchecker/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/updater/daemonchecker/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/updater/daemonchecker/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/updater/daemonchecker/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/updater/localapi/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/updater/localapi/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/updater/localapi/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/updater/localapi/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/updater/localapiclient/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/updater/localapiclient/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/updater/localapiclient/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/updater/ssistatus/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/updater/ssistatus/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/updater/ssistatus/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/updater/telemetry/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/updater/telemetry/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/updater/telemetry/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/updater/telemetry/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/updater/updater/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/updater/updater/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/updater/updater/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/workloadselection/def) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/workloadselection/fx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/comp/workloadselection/impl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/internal/third_party/client-go/tools/leaderelection/resourcelock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/internal/third_party/golang/expansion) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/internal/third_party/kubernetes/pkg/kubelet/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/internal/tools) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/internal/tools/gotest-custom) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/internal/tools/independent-lint) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/internal/tools/modformatter) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/internal/tools/modparser) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/internal/tools/proto) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/internal/tools/worksynchronizer) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/aggregator) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/aggregator/ckey) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/aggregator/internal/tags) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/aggregator/internal/util) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/aggregator/mocksender) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/aggregator/sender) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/api) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/api/coverage) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/api/security) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/api/security/cert) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/api/util) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/api/version) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/cli/standalone) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/cli/subcommands/autoscalerlist) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/cli/subcommands/check) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/cli/subcommands/clusterchecks) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/cli/subcommands/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/cli/subcommands/dcaconfigcheck) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/cli/subcommands/dcaflare) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/cli/subcommands/experimental) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/cli/subcommands/health) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/cli/subcommands/processchecks) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/cli/subcommands/taggerlist) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/cli/subcommands/version) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/cli/subcommands/workloadfilter) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/cli/subcommands/workloadlist) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/cloudfoundry/containertagger) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/controllers/secret) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/controllers/webhook) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/metrics) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/mutate) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/mutate/agent_sidecar) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/mutate/appsec) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/mutate/autoinstrumentation) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/mutate/autoinstrumentation/annotation) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/mutate/autoinstrumentation/imageresolver) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/mutate/autoinstrumentation/libraryinjection) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/mutate/autoscaling) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/mutate/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/mutate/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/mutate/cwsinstrumentation) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/mutate/cwsinstrumentation/k8scp) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/mutate/cwsinstrumentation/k8sexec) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/mutate/ncclprofiler) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/mutate/spot) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/mutate/tagsfromlabels) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/patch) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/probe) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/validate) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/validate/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/validate/datadoginstrumentation) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/admission/validate/kubernetesadmissionevents) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/api) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/api/v1) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/appsec) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/appsec/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/appsec/envoygateway) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/appsec/istio) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/appsec/nginx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/appsec/sidecar) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/autoscaling) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/autoscaling/cluster) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/autoscaling/cluster/model) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/autoscaling/cluster/spot) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/autoscaling/custommetrics) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/autoscaling/externalmetrics) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/autoscaling/externalmetrics/model) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/autoscaling/workload) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/autoscaling/workload/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/autoscaling/workload/external) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/autoscaling/workload/loadstore) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/autoscaling/workload/local) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/autoscaling/workload/metrics) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/autoscaling/workload/model) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/autoscaling/workload/profile) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/autoscaling/workload/provider) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/clusterchecks) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/clusterchecks/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/evictor) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/instrumentation) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/instrumentation/handlers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/kubeactions) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/kubeactions/executors) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/languagedetection) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/mcp) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/mcp/tools) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/metricsstatus) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/metricsstore) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/orchestrator) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/patcher) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/clusteragent/telemetry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/aggregator) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/check) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/check/defaults) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/check/id) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/check/stats) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/check/stub) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/agentprofiling) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/cloud/hostinfo) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/cluster) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/cluster/helm) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/cluster/ksm) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/cluster/ksm/customresources) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/cluster/kubernetesapiserver) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/cluster/orchestrator) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/cluster/orchestrator/collectors) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/cluster/orchestrator/collectors/ecs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/cluster/orchestrator/collectors/inventory) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/cluster/orchestrator/collectors/k8s) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/cluster/orchestrator/discovery) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/cluster/orchestrator/processors) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/cluster/orchestrator/processors/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/cluster/orchestrator/processors/ecs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/cluster/orchestrator/processors/k8s) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/cluster/orchestrator/processors/k8s/pod_tag_provider) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/cluster/orchestrator/processorstest) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/cluster/orchestrator/transformers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/cluster/orchestrator/transformers/ecs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/cluster/orchestrator/transformers/k8s) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/cluster/orchestrator/util) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/containerimage) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/containerlifecycle) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/containers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/containers/containerd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/containers/cri) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/containers/csi_driver) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/containers/docker) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/containers/generic) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/containers/kata) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/containers/kubelet) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/containers/kubelet/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/containers/kubelet/common/testing) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/containers/kubelet/provider/cadvisor) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/containers/kubelet/provider/health) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/containers/kubelet/provider/kubelet) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/containers/kubelet/provider/node) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/containers/kubelet/provider/pod) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/containers/kubelet/provider/probe) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/containers/kubelet/provider/prometheus) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/containers/kubelet/provider/slis) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/containers/kubelet/provider/summary) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/discovery) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/ebpf) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/ebpf/noisyneighbor) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/ebpf/oomkill) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/ebpf/probe/ebpfcheck) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/ebpf/probe/ebpfcheck/model) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/ebpf/probe/noisyneighbor) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/ebpf/probe/noisyneighbor/model) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/ebpf/probe/oomkill) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/ebpf/probe/oomkill/model) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/ebpf/probe/tcpqueuelength) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/ebpf/probe/tcpqueuelength/model) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/ebpf/tcpqueuelength) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/embed/apm) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/embed/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/embed/process) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/gpu) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/gpu/integrationtests) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/gpu/model) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/gpu/nccl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/gpu/nvidia) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/gpu/spec) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/net) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/net/network) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/net/networkv2) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/net/ntp) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/net/wlan) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/network-devices/cisco-sdwan) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/network-devices/cisco-sdwan/client) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/network-devices/cisco-sdwan/client/fixtures) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/network-devices/cisco-sdwan/payload) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/network-devices/cisco-sdwan/report) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/network-devices/versa) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/network-devices/versa/client) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/network-devices/versa/client/fixtures) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/network-devices/versa/payload) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/network-devices/versa/report) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/networkconfigmanagement) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/networkpath) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/nvidia/jetson) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/oracle) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/oracle/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/oracle/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/orchestrator) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/orchestrator/ecs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/orchestrator/kubeletconfig) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/orchestrator/pod) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/sbom) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/snmp) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/snmp/internal/checkconfig) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/snmp/internal/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/snmp/internal/devicecheck) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/snmp/internal/discovery) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/snmp/internal/fetch) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/snmp/internal/lldp) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/snmp/internal/metadata) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/snmp/internal/profile) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/snmp/internal/report) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/snmp/internal/session) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/snmp/internal/valuestore) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/snmp/status) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/system) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/system/battery) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/system/cpu/cpu) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/system/cpu/load) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/system/disk/disk) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/system/disk/diskv2) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/system/disk/io) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/system/filehandles) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/system/memory) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/system/uptime) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/system/wincrashdetect) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/system/wincrashdetect/probe) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/system/windowscertificate) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/system/winkmem) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/system/winproc) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/systemd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/corechecks/telemetry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/externalhost) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/loaders) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/python) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/runner) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/runner/expvars) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/runner/tracker) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/scheduler) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/sharedlibrary/ffi) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/sharedlibrary/sharedlibraryimpl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/collector/worker) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/commonchecks) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/compliance) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/compliance/aptconfig) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/compliance/cli) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/compliance/dbconfig) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/compliance/k8sconfig) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/compliance/metrics) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/compliance/scap) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/compliance/statusregistry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/compliance/tests) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/compliance/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/compliance/utils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/autodiscovery) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/basic) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/buildschema) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/create) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/env) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/fetcher) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/fetcher/sysprobe) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/fetcher/tracers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/helper) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/legacy) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/model) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/nodetreemodel) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/remote) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/remote/api) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/remote/client) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/remote/data) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/remote/meta) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/remote/service) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/remote/uptane) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/schema) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/settings) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/settings/http) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/setup) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/setup/constants) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/structure) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/teeconfig) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/utils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/config/viperconfig) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/containerlifecycle) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/databasemonitoring/aws) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/diagnose/connectivity) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/diagnose/firewallscanner) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/diagnose/ports) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/discovery/core) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/discovery/language) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/discovery/model) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/discovery/module) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/discovery/module/splite) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/discovery/tracermetadata) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/discovery/tracermetadata/language) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/discovery/tracermetadata/model) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/discovery/usm) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/actuator) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/compiler) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/decode) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/dispatcher) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/dwarf) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/dwarf/dwarfutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/dwarf/loclist) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/dyninsttest) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/eventbuf) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/exprlang) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/gosym) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/gosymname) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/gotype) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/gotype/gotypeprinter) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/htlhash) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/ir) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/irgen) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/irprinter) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/jsonprune) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/loader) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/module) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/module/tombstone) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/object) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/output) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/process) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/procsubscribe) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/procsubscribe/procscan) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/rcjson) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/symbol) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/symdb) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/symdb/symdbprinter) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/symdb/uploader) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/testprogs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/testprogs/progs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/testprogs/progs/sample/lib) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/testprogs/progs/sample/lib.v2) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/testprogs/progs/sample/lib2) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/trietest) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/uploader) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/dyninst/uprobe) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/ebpf) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/ebpf/bytecode) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/ebpf/bytecode/runtime) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/ebpf/compiler) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/ebpf/ebpftest) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/ebpf/features) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/ebpf/kernelbugs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/ebpf/maps) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/ebpf/modifiers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/ebpf/names) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/ebpf/perf) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/ebpf/prebuilt) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/ebpf/telemetry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/ebpf/uprobes) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/ebpf/uprobes/testutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/ebpf/verifier) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/errors) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/eventmonitor) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/eventmonitor/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/eventmonitor/consumers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/eventmonitor/consumers/testutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/eventmonitor/examples) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/eventmonitor/testutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fips) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/flare) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/flare/clusteragent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/flare/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/flare/priviledged) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/flare/securityagent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/daemon) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/bootstrap) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/commands) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/db) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/env) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/errors) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/exec) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/fixtures) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/installinfo) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/msi) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/oci) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/packages) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/packages/apminject) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/packages/embedded) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/packages/exec) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/packages/extensions) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/packages/fapolicyd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/packages/file) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/packages/integrations) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/packages/packagemanager) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/packages/selinux) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/packages/service) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/packages/service/systemd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/packages/service/sysvinit) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/packages/service/upstart) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/packages/service/windows) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/packages/ssi) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/packages/user) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/packages/user/windows) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/paths) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/repository) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/setup) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/setup/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/setup/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/setup/defaultscript) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/setup/djm) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/symlink) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/tar) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/fleet/installer/telemetry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/gohai) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/gohai/cpu) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/gohai/filesystem) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/gohai/memory) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/gohai/network) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/gohai/platform) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/gohai/processes) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/gohai/processes/gops) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/gohai/utils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/gpu) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/gpu/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/gpu/config/consts) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/gpu/containers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/gpu/cuda) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/gpu/cuda/testutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/gpu/ebpf) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/gpu/integrationtests) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/gpu/prm) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/gpu/safenvml) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/gpu/safenvml/testutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/gpu/tags) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/gpu/testutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/hosttags) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/inventory/software) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/inventory/systeminfo) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/jmxfetch) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/kubestatemetrics/builder) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/kubestatemetrics/store) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/languagedetection) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/languagedetection/internal/detectors) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/languagedetection/internal/detectors/privileged) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/languagedetection/languagemodels) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/languagedetection/privileged) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/languagedetection/util) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logonduration) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/diagnostic) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/internal/decoder) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/internal/decoder/preprocessor) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/internal/framer) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/internal/parsers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/internal/parsers/dockerfile) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/internal/parsers/dockerstream) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/internal/parsers/encodedtext) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/internal/parsers/integrations) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/internal/parsers/kubernetes) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/internal/parsers/noop) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/internal/parsers/syslog) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/internal/tag) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/internal/util) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/internal/util/adlistener) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/internal/util/containersorpods) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/internal/util/opener) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/launchers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/launchers/channel) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/launchers/container) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/launchers/container/tailerfactory) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/launchers/container/tailerfactory/tailers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/launchers/file) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/launchers/file/provider) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/launchers/integration) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/launchers/journald) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/launchers/listener) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/launchers/windowsevent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/message) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/schedulers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/schedulers/ad) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/schedulers/channel) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/service) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/sources) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/status) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/status/statusinterface) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/status/utils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/tailers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/tailers/channel) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/tailers/container) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/tailers/file) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/tailers/journald) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/tailers/socket) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/tailers/windowsevent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/util/opener) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/util/testutils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/logs/util/windowsevent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/metrics) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/metrics/event) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/metrics/servicecheck) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/config/sysctl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/containers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/dns) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/driver) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/ebpf) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/ebpf/probes) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/encoding) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/encoding/marshal) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/encoding/unmarshal) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/events) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/filter) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/go/asmscan) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/go/bininspect) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/go/binversion) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/go/dwarfutils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/go/dwarfutils/locexpr) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/go/goid) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/go/goversion) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/go/lutgen) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/go/rungo) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/go/rungo/matrix) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/indexedset) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/netlink) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/netlink/testutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/payload) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/protocols) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/protocols/amqp) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/protocols/events) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/protocols/http) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/protocols/http/debugging) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/protocols/http/gotls) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/protocols/http/gotls/lookup) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/protocols/http/testutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/protocols/http2) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/protocols/kafka) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/protocols/kafka/debugging) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/protocols/mongo) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/protocols/mysql) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/protocols/postgres) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/protocols/postgres/debugging) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/protocols/postgres/ebpf) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/protocols/redis) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/protocols/redis/debugging) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/protocols/telemetry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/protocols/testutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/protocols/tls) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/protocols/tls/gotls/testutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/protocols/tls/nodejs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/remoteservice) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/sender) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/slice) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/testutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/tracer) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/tracer/connection) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/tracer/connection/ebpfless) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/tracer/connection/fentry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/tracer/connection/kprobe) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/tracer/connection/sk) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/tracer/connection/ssl-uprobes) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/tracer/connection/util) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/tracer/networkfilter) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/tracer/offsetguess) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/tracer/testutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/tracer/testutil/proxy) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/tracer/testutil/testdns) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/usm) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/usm/buildmode) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/usm/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/usm/consts) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/usm/maps) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/usm/procnet) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/usm/sharedlibraries) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/usm/sharedlibraries/testutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/usm/state) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/usm/tests) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/usm/testutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/usm/testutil/grpc) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/network/usm/utils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/networkconfigmanagement/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/networkconfigmanagement/profile) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/networkconfigmanagement/remote) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/networkconfigmanagement/report) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/networkconfigmanagement/sender) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/networkconfigmanagement/store) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/networkconfigmanagement/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/networkdevice/diagnoses) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/networkdevice/integrations) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/networkdevice/metadata) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/networkdevice/pinger) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/networkdevice/profile) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/networkdevice/profile/profiledefinition) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/networkdevice/profile/profiledefinition/normalize_cmd/cmd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/networkdevice/profile/profiledefinition/schema) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/networkdevice/sender) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/networkdevice/testutils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/networkdevice/utils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/networkpath/metricsender) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/networkpath/payload) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/networkpath/telemetry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/networkpath/traceroute/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/networkpath/traceroute/runner) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/obfuscate) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/inframetadata) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/inframetadata/gohai) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/inframetadata/gohai/internal/gohaitest) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/inframetadata/internal/hostmap) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/inframetadata/internal/testutils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/inframetadata/payload) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/attributes) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/attributes/azure) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/attributes/ec2) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/attributes/gcp) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/attributes/internal/testutils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/attributes/source) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/logs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/metrics) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/metrics/internal/instrumentationlibrary) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/metrics/internal/instrumentationscope) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/metrics/internal/utils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/rum) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/orchestrator) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/orchestrator/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/orchestrator/model) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/orchestrator/util) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/persistentcache) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/pidfile) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/adapters/actions) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/adapters/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/adapters/constants) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/adapters/httpclient) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/adapters/logging) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/adapters/modes) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/adapters/parversion) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/adapters/rcclient) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/adapters/regions) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/adapters/tmpl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/adapters/workflowjsonschema) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/autoconnections) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundle-support) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundle-support/gitlab) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundle-support/httpclient) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundle-support/kubernetes) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/gitlab/branches) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/gitlab/commits) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/gitlab/customattributes) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/gitlab/deployments) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/gitlab/environments) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/gitlab/graphql) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/gitlab/groups) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/gitlab/issues) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/gitlab/jobs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/gitlab/labels) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/gitlab/members) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/gitlab/mergerequests) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/gitlab/notes) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/gitlab/pipelines) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/gitlab/projects) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/gitlab/protectedbranches) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/gitlab/repositories) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/gitlab/repositoryfiles) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/gitlab/tags) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/gitlab/users) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/http) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/jenkins) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/kubernetes/apiextensions) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/kubernetes/apps) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/kubernetes/batch) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/kubernetes/core) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/kubernetes/customresources) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/kubernetes/discovery) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/mongodb) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/remoteaction) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/remoteaction/networks) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/remoteaction/rshell) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/script) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/bundles/temporal) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/credentials/resolver) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/enrollment) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/libs/connection) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/libs/par) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/libs/privateconnection) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/libs/tempfile) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/observability) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/opms) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/opms/testing) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/runners) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/task-verifier) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privateactionrunner/util) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privileged-logs/client) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privileged-logs/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privileged-logs/module) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/privileged-logs/test) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/checks) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/checks/mocks) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/encoding) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/encoding/request) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/metadata) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/metadata/parser) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/metadata/parser/java) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/metadata/parser/nodejs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/metadata/workloadmeta) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/metadata/workloadmeta/collector) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/monitor) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/net) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/net/resolver) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/procutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/procutil/mocks) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/runner) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/runner/endpoint) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/runner/mocks) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/status) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/subscribers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/util) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/util/api) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/util/api/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/util/api/headers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/util/containers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/util/containers/mocks) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/util/coreagent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/process/util/status) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/proto) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/proto/msgpgo) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/proto/pbgo/core) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/proto/pbgo/dogstatsdhttp) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/proto/pbgo/languagedetection) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/proto/pbgo/mocks/core) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/proto/pbgo/privateactionrunner/actionsclient) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/proto/pbgo/privateactionrunner/errorcode) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/proto/pbgo/privateactionrunner/privateactions) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/proto/pbgo/process) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/proto/pbgo/sbom) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/proto/pbgo/trace) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/proto/pbgo/trace/idx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/proto/utils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/redact) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/remoteconfig/state) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/remoteconfig/state/products/apmsampling) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/remoteflags) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/runtime) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/sbom) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/sbom/bomconvert) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/sbom/collectors) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/sbom/collectors/containerd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/sbom/collectors/crio) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/sbom/collectors/docker) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/sbom/collectors/host) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/sbom/collectors/procfs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/sbom/scanner) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/sbom/telemetry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/sbom/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/agent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/agent/mocks) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/clihelpers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/common/usergrouputils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/ebpf) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/ebpf/kernel) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/ebpf/probes) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/ebpf/probes/rawpacket) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/events) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/generators/accessors/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/generators/accessors/doc) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/metrics) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/module) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/probe) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/probe/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/probe/constantfetch) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/probe/erpc) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/probe/eventstream) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/probe/eventstream/reorderer) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/probe/eventstream/ringbuffer) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/probe/kfilters) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/probe/managerhelper) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/probe/monitors/approver) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/probe/monitors/cgroups) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/probe/monitors/discarder) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/probe/monitors/dns) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/probe/monitors/eventsample) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/probe/monitors/syscalls) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/probe/procfs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/probe/selftests) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/probe/sysctl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/process_list) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/process_list/activity_tree) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/process_list/process_resolver) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/proto/api) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/proto/api/mocks) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/proto/api/transform) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/proto/ebpfless) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/ptracer) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/rconfig) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/reporter) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/resolvers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/resolvers/cgroup) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/resolvers/cgroup/model) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/resolvers/dentry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/resolvers/dns) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/resolvers/envvars) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/resolvers/file) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/resolvers/hash) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/resolvers/mount) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/resolvers/netns) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/resolvers/path) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/resolvers/process) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/resolvers/sbom) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/resolvers/sbom/collectorv2) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/resolvers/sbom/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/resolvers/securitydescriptors) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/resolvers/selinux) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/resolvers/sign) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/resolvers/syscallctx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/resolvers/tags) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/resolvers/tc) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/resolvers/usergroup) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/resolvers/usersessions) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/rules) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/rules/bundled) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/rules/filtermodel) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/rules/monitor) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/secl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/secl/args) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/secl/compiler/ast) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/secl/compiler/eval) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/secl/containerutils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/secl/log) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/secl/model) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/secl/model/sharedconsts) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/secl/model/usersession) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/secl/model/utils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/secl/rules) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/secl/rules/filter) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/secl/schemas) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/secl/utils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/secl/validators) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/seclog) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/seclwin) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/seclwin/model) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/security_profile) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/security_profile/activity_tree) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/security_profile/activity_tree/metadata) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/security_profile/dump) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/security_profile/profile) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/security_profile/storage) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/security_profile/storage/backend) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/serializers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/telemetry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/tests) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/tests/statsdclient) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/tests/testutils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/utils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/utils/cache) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/utils/cgroup) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/utils/grpc) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/utils/k8sutils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/utils/lru) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/utils/lru/internal) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/utils/lru/simplelru) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/security/utils/pathutils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/serializer) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/serializer/internal/metrics) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/serializer/internal/stream) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/serializer/marshaler) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/serializer/mocks) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/serializer/split) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/serializer/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/serverless) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/serverless/env) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/serverless/logs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/serverless/metrics) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/serverless/otlp) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/serverless/streamlogs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/serverless/tags) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/serverless/trace) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/serverless/trace/modifier) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/snmp) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/snmp/devicededuper) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/snmp/gosnmplib) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/snmp/snmpintegration) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/snmp/snmpparse) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/snmp/utils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/ssi/testutils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/status) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/status/clusteragent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/status/clusteragent/hostname) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/status/collector) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/status/endpoints) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/status/health) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/status/httpproxy) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/status/jmx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/status/render) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/status/systemprobe) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/system-probe/api/client) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/system-probe/api/module) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/system-probe/api/server) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/system-probe/api/server/testutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/system-probe/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/system-probe/config/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/system-probe/utils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/tagger) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/tagger/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/tagset) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/template) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/template/html) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/template/internal/fmtsort) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/template/text) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/agent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/api) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/api/apiutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/api/internal/header) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/api/loader) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/containertags) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/event) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/filters) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/info) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/log) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/otel) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/otel/stats) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/otel/traceutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/payload) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/pb) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/remoteconfighandler) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/sampler) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/semantics) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/stats) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/telemetry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/teststatsd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/testutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/timing) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/traceutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/traceutil/normalize) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/transform) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/version) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/watchdog) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/trace/writer) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/aggregatingqueue) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/archive) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/atomicstats) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/aws/creds) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/aws/creds/internal) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/backoff) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/buf) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/cache) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/cachedfetch) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/cgroups) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/cgroups/memorymonitor) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/cli) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/cloudproviders) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/cloudproviders/alibaba) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/cloudproviders/azure) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/cloudproviders/cloudfoundry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/cloudproviders/gce) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/cloudproviders/ibm) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/cloudproviders/kubernetes) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/cloudproviders/network) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/cloudproviders/oracle) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/cloudproviders/tencent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/clusteragent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/compression) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/compression/impl-gzip) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/compression/impl-noop) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/compression/impl-zlib) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/compression/impl-zstd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/compression/impl-zstd-nocgo) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/compression/selector) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/containerd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/containerd/fake) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/containers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/containers/cri) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/containers/cri/crimock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/containers/image) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/containers/metadata) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/containers/metrics) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/containers/metrics/containerd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/containers/metrics/cri) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/containers/metrics/docker) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/containers/metrics/ecsfargate) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/containers/metrics/ecsmanagedinstances) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/containers/metrics/kubelet) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/containers/metrics/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/containers/metrics/provider) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/containers/metrics/system) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/coredump) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/crashreport) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/crio) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/defaultpaths) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/dmi) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/docker) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/docker/fake) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/ec2) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/ec2/internal) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/ec2/tags) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/ecs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/ecs/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/ecs/metadata) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/ecs/metadata/testutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/ecs/metadata/v1) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/ecs/metadata/v2) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/ecs/metadata/v3or4) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/ecs/telemetry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/executable) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/fargate) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/filesystem) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/flavor) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/funcs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/fxutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/fxutil/logging) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/goroutinesdump) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/gpu) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/grpc) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/grpc/context) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/hostinfo) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/hostname) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/hostname/validate) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/hostport) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/http) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/input) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/installinfo) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/intern) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/json) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/jsonquery) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kernel) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kernel/headers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kernel/headers/download/apt) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kernel/headers/download/cos) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kernel/headers/download/extract) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kernel/headers/download/rpm) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kernel/headers/download/rpm/dnfv2) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kernel/headers/download/rpm/dnfv2/backend) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kernel/headers/download/rpm/dnfv2/internal/utils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kernel/headers/download/rpm/dnfv2/repo) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kernel/headers/download/rpm/dnfv2/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kernel/headers/download/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kernel/headers/download/wsl) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kernel/headers/download/xmlite) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kernel/netns) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/ktime) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kubelet) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kubernetes) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kubernetes/apiserver) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kubernetes/apiserver/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kubernetes/apiserver/common/namespace) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kubernetes/apiserver/controllers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kubernetes/apiserver/leaderelection) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kubernetes/apiserver/leaderelection/metrics) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kubernetes/autoscalers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kubernetes/certificate) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kubernetes/cloudprovider) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kubernetes/clusterinfo) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kubernetes/clustername) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kubernetes/hostinfo) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kubernetes/kubelet) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/kubernetes/kubelet/mock) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/log) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/log/setup) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/log/slog) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/log/slog/filewriter) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/log/slog/formatters) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/log/slog/handlers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/log/syslog) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/log/types) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/log/zap) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/lsof) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/maps) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/net) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/option) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/os) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/otel) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/pdhutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/podman) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/pointer) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/port) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/port/portlist) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/procfilestats) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/profiling) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/prometheus) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/quantile) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/quantile/sketchtest) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/quantile/summary) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/retry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/safeelf) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/scrubber) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/size) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/slices) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/sort) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/startstop) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/stat) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/statstracker) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/strings) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/subscriptions) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/sync) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/system) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/system/socket) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/tags) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/testutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/testutil/docker) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/testutil/flake) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/tmplvar) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/trie) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/trivy) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/trivy/walker) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/utilizationtracker) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/uuid) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/winutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/winutil/datadoginterop) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/winutil/etw) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/winutil/eventlog/api) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/winutil/eventlog/api/fake) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/winutil/eventlog/api/windows) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/winutil/eventlog/bookmark) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/winutil/eventlog/publishermetadatacache) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/winutil/eventlog/reporter) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/winutil/eventlog/session) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/winutil/eventlog/subscription) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/winutil/eventlog/test) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/winutil/iisconfig) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/winutil/iphelper) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/winutil/messagestrings) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/winutil/servicemain) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/winutil/winmem) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/workqueue/telemetry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/util/xc) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/version) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/windowsdriver/ddinjector) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/windowsdriver/driver) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/windowsdriver/olreader) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/pkg/windowsdriver/procmon) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/rtloader/test/aggregator) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/rtloader/test/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/rtloader/test/containers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/rtloader/test/datadog_agent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/rtloader/test/helpers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/rtloader/test/init) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/rtloader/test/kubeutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/rtloader/test/rtloader) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/rtloader/test/tagger) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/rtloader/test/util) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/rtloader/test/uutil) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/common/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/common/namer) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/common/utils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/activedirectory) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/command) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/agent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/agent/helm) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/agent/k8ssidecar) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/agentparams) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/agentparams/filepermissions) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/agentparams/msi) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/agentwithoperatorparams) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/apps) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/apps/aspnetsample) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/apps/cpustress) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/apps/dda) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/apps/dogstatsd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/apps/etcd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/apps/jmxfetch) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/apps/logger) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/apps/mutatedbyadmissioncontroller) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/apps/nginx) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/apps/nginx/k8s) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/apps/npm-tools) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/apps/prometheus) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/apps/redis) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/apps/singlestep) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/apps/tracegen) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/csi-driver) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/dockeragentparams) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/dogstatsd-standalone) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/ecsagentparams) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/fakeintake) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/kubernetesagentparams) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/operator) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/operatorparams) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/otel-standalone) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/datadog/updater) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/docker) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/ecs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/iis) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/kubernetes) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/kubernetes/argorollouts) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/kubernetes/cilium) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/kubernetes/istio) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/kubernetes/k8sapply) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/kubernetes/nvidia) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/kubernetes/vpa) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/os) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/remote) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/windows/command) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/windows/defender) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/windows/fipsmode) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/components/windows/testsigning) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/registry) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/resources/aws) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/resources/aws/ec2) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/resources/aws/ecs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/resources/aws/eks) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/resources/aws/iam) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/resources/azure) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/resources/azure/aks) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/resources/azure/compute) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/resources/gcp) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/resources/gcp/compute) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/resources/gcp/gke) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/resources/helm) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/resources/hyperv) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/resources/local) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/resources/local/podman) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/aws/ec2) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/aws/ec2/windows) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/aws/ec2docker) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/aws/ecs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/aws/eks) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/aws/fakeintake) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/aws/gensim-eks) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/aws/installer) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/aws/kindvm) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/aws/microVMs/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/aws/microVMs/microvms) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/aws/microVMs/microvms/resources) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/aws/microVMs/vmconfig) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/azure/aks) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/azure/compute) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/azure/compute/run) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/azure/fakeintake) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/gcp/compute) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/gcp/compute/run) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/gcp/fakeintake) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/gcp/gke) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/gcp/openshiftvm) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/hyperv) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/local/podman) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/local/podman/run) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/scenarios/outputs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/components) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/e2e) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/environments) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/provisioners) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/provisioners/aws/docker) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/provisioners/aws/ecs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/provisioners/aws/host) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/provisioners/aws/host/windows) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/provisioners/aws/kubernetes) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/provisioners/aws/kubernetes/eks) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/provisioners/aws/kubernetes/kindvm) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/provisioners/azure/host/linux) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/provisioners/azure/host/windows) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/provisioners/azure/kubernetes) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/provisioners/gcp/host/linux) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/provisioners/gcp/kubernetes) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/provisioners/gcp/kubernetes/openshiftvm) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/provisioners/local/host) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/provisioners/local/kubernetes) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/runner) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/runner/parameters) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/testcommon/check) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/utils/clients) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/utils/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/utils/e2e/client) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/utils/e2e/client/agentclient) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/utils/e2e/client/agentclientparams) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/utils/e2e/client/ecs) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/utils/infra) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/utils/k8s) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/utils/optional) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/e2e-framework/testing/utils/ssh) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/fakeintake) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/fakeintake/aggregator) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/fakeintake/api) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/fakeintake/client) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/fakeintake/client/flare) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/fakeintake/cmd/client/cmd) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/fakeintake/fixtures) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/fakeintake/server) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/fakeintake/server/rcstore) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/fakeintake/server/serverstore) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/system-probe) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/system-probe/connector/metric) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/system-probe/connector/sshtools) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/agent-configuration) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/agent-configuration/secretsutils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/agent-health) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/agent-log-pipelines/kindfilelogging) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/agent-log-pipelines/utils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/agent-metric-pipelines/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/agent-metric-pipelines/dogstatsd-unit) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/agent-metric-pipelines/jmxfetch) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/agent-metric-pipelines/metric-filterlist) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/agent-platform/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/agent-platform/common/bound-port) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/agent-platform/common/file-manager) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/agent-platform/common/helper) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/agent-platform/common/pkg-manager) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/agent-platform/common/process) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/agent-platform/common/svc-manager) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/agent-platform/install) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/agent-platform/install/installparams) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/agent-platform/platforms) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/agent-runtimes) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/agent-subcommands/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/agent-subcommands/flare) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/apm) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/containers) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/cws) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/cws/api) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/cws/config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/fips-compliance) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/fleet/agent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/fleet/backend) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/fleet/host) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/fleet/installer) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/fleet/suite) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/gpu) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/installer/host) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/installer/unix) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/installer/windows) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/installer/windows/consts) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/installer/windows/remote-host-assertions) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/installer/windows/suite-assertions) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/ndm/snmp) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/npm) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/orchestrator) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/otel/utils) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/privateactionrunner) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/process) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/remote-config) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/ssi) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/ssi-gradual-rollout) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/windows) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/windows/common) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/windows/common/agent) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/windows/common/agent/installers/v2) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/windows/common/pipeline) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/windows/components/certificatehost) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/windows/install-test) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/windows/install-test/service-test) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/new-e2e/tests/windows/service-test) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/test/otel) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/tools/build-ddot-byoc) = %{version}
Provides:       go(github.com/DataDog/datadog-agent/tools/retry_file_dump) = %{version}

Requires:       go(cloud.google.com/go/compute)
Requires:       go(cloud.google.com/go/compute/metadata)
Requires:       go(code.cloudfoundry.org/bbs)
Requires:       go(code.cloudfoundry.org/garden)
Requires:       go(code.cloudfoundry.org/lager)
Requires:       go(dario.cat/mergo)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/azidentity)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/security/keyvault/azsecrets)
Requires:       go(github.com/CycloneDX/cyclonedx-go)
Requires:       go(github.com/DataDog/agent-payload/v5)
Requires:       go(github.com/DataDog/datadog-api-client-go)
Requires:       go(github.com/DataDog/datadog-api-client-go/v2)
Requires:       go(github.com/DataDog/datadog-go/v5)
Requires:       go(github.com/DataDog/datadog-operator/api)
Requires:       go(github.com/DataDog/datadog-traceroute)
Requires:       go(github.com/DataDog/dd-trace-go/contrib/net/http/v2)
Requires:       go(github.com/DataDog/dd-trace-go/v2)
Requires:       go(github.com/DataDog/ddtrivy)
Requires:       go(github.com/DataDog/ebpf-manager)
Requires:       go(github.com/DataDog/go-acl)
Requires:       go(github.com/DataDog/go-sqllexer)
Requires:       go(github.com/DataDog/go-tuf)
Requires:       go(github.com/DataDog/jsonapi)
Requires:       go(github.com/DataDog/orchestrion)
Requires:       go(github.com/DataDog/rshell)
Requires:       go(github.com/DataDog/sketches-go)
Requires:       go(github.com/DataDog/viper)
Requires:       go(github.com/DataDog/watermarkpodautoscaler/apis)
Requires:       go(github.com/DataDog/zstd)
Requires:       go(github.com/Masterminds/semver/v3)
Requires:       go(github.com/Masterminds/sprig/v3)
Requires:       go(github.com/Microsoft/go-winio)
Requires:       go(github.com/Microsoft/hcsshim)
Requires:       go(github.com/NVIDIA/go-nvml)
Requires:       go(github.com/ProtonMail/go-crypto)
Requires:       go(github.com/aarzilli/whydeadcode)
Requires:       go(github.com/acobaugh/osrelease)
Requires:       go(github.com/alecthomas/participle)
Requires:       go(github.com/alecthomas/units)
Requires:       go(github.com/alessio/shellescape)
Requires:       go(github.com/aptly-dev/aptly)
Requires:       go(github.com/aquasecurity/trivy)
Requires:       go(github.com/aquasecurity/trivy-db)
Requires:       go(github.com/avast/retry-go/v4)
Requires:       go(github.com/aws/aws-sdk-go-v2)
Requires:       go(github.com/aws/aws-sdk-go-v2/config)
Requires:       go(github.com/aws/aws-sdk-go-v2/credentials)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/ec2)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/ecr)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/ecs)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/eks)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/rds)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/s3)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/secretsmanager)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/ssm)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/sts)
Requires:       go(github.com/aws/karpenter-provider-aws)
Requires:       go(github.com/aws/session-manager-plugin)
Requires:       go(github.com/aymerick/raymond)
Requires:       go(github.com/bazelbuild/bazelisk)
Requires:       go(github.com/bazelbuild/rules_go)
Requires:       go(github.com/beevik/ntp)
Requires:       go(github.com/benbjohnson/clock)
Requires:       go(github.com/bhmj/jsonslice)
Requires:       go(github.com/blabber/go-freebsd-sysctl)
Requires:       go(github.com/bmatcuk/doublestar/v4)
Requires:       go(github.com/cenkalti/backoff/v5)
Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/charlievieth/strcase)
Requires:       go(github.com/cilium/ebpf)
Requires:       go(github.com/clbanning/mxj)
Requires:       go(github.com/cloudflare/cbpfc)
Requires:       go(github.com/cloudfoundry-community/go-cfclient/v2)
Requires:       go(github.com/containerd/cgroups/v3)
Requires:       go(github.com/containerd/containerd)
Requires:       go(github.com/containerd/containerd/api)
Requires:       go(github.com/containerd/errdefs)
Requires:       go(github.com/containerd/typeurl/v2)
Requires:       go(github.com/containernetworking/cni)
Requires:       go(github.com/coreos/go-semver)
Requires:       go(github.com/coreos/go-systemd/v22)
Requires:       go(github.com/cri-o/ocicni)
Requires:       go(github.com/cyphar/filepath-securejoin)
Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/digitalocean/go-libvirt)
Requires:       go(github.com/distribution/reference)
Requires:       go(github.com/docker/cli)
Requires:       go(github.com/dustin/go-humanize)
Requires:       go(github.com/elastic/go-freelru)
Requires:       go(github.com/elastic/go-libaudit/v2)
Requires:       go(github.com/elastic/go-seccomp-bpf)
Requires:       go(github.com/envoyproxy/gateway)
Requires:       go(github.com/evanphx/json-patch/v5)
Requires:       go(github.com/fatih/color)
Requires:       go(github.com/fatih/structtag)
Requires:       go(github.com/favadi/protoc-go-inject-tag)
Requires:       go(github.com/frapposelli/wwhrd)
Requires:       go(github.com/freddierice/go-losetup)
Requires:       go(github.com/fsnotify/fsnotify)
Requires:       go(github.com/ghodss/yaml)
Requires:       go(github.com/glaslos/ssdeep)
Requires:       go(github.com/go-delve/delve)
Requires:       go(github.com/go-enry/go-license-detector/v4)
Requires:       go(github.com/go-ini/ini)
Requires:       go(github.com/go-jose/go-jose/v4)
Requires:       go(github.com/go-json-experiment/json)
Requires:       go(github.com/go-ole/go-ole)
Requires:       go(github.com/go-sql-driver/mysql)
Requires:       go(github.com/go-viper/mapstructure/v2)
Requires:       go(github.com/gobwas/glob)
Requires:       go(github.com/gocomply/scap)
Requires:       go(github.com/godbus/dbus/v5)
Requires:       go(github.com/godror/godror)
Requires:       go(github.com/gofrs/flock)
Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/golang-jwt/jwt/v5)
Requires:       go(github.com/golang/groupcache)
Requires:       go(github.com/golang/mock)
Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/golangci/golangci-lint/v2)
Requires:       go(github.com/google/btree)
Requires:       go(github.com/google/cel-go)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/go-containerregistry)
Requires:       go(github.com/google/gopacket)
Requires:       go(github.com/google/shlex)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/gorilla/handlers)
Requires:       go(github.com/gorilla/mux)
Requires:       go(github.com/gorilla/websocket)
Requires:       go(github.com/gosnmp/gosnmp)
Requires:       go(github.com/goware/modvendor)
Requires:       go(github.com/grpc-ecosystem/go-grpc-middleware)
Requires:       go(github.com/h2non/filetype)
Requires:       go(github.com/hairyhenderson/go-codeowners)
Requires:       go(github.com/hashicorp/consul/api)
Requires:       go(github.com/hashicorp/go-multierror)
Requires:       go(github.com/hashicorp/go-retryablehttp)
Requires:       go(github.com/hashicorp/go-version)
Requires:       go(github.com/hashicorp/golang-lru/v2)
Requires:       go(github.com/hashicorp/vault/api)
Requires:       go(github.com/hashicorp/vault/api/auth/approle)
Requires:       go(github.com/hashicorp/vault/api/auth/aws)
Requires:       go(github.com/hashicorp/vault/api/auth/ldap)
Requires:       go(github.com/hashicorp/vault/api/auth/userpass)
Requires:       go(github.com/imdario/mergo)
Requires:       go(github.com/invopop/jsonschema)
Requires:       go(github.com/itchyny/gojq)
Requires:       go(github.com/jackc/pgx/v5)
Requires:       go(github.com/jellydator/ttlcache/v3)
Requires:       go(github.com/jmoiron/sqlx)
Requires:       go(github.com/jonboulle/clockwork)
Requires:       go(github.com/json-iterator/go)
Requires:       go(github.com/judwhite/go-svc)
Requires:       go(github.com/justincormack/go-memfd)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/knqyf263/go-deb-version)
Requires:       go(github.com/knqyf263/go-rpmdb)
Requires:       go(github.com/kouhin/envflag)
Requires:       go(github.com/kr/pretty)
Requires:       go(github.com/lorenzosaino/go-sysctl)
Requires:       go(github.com/lxn/walk)
Requires:       go(github.com/lxn/win)
Requires:       go(github.com/mailru/easyjson)
Requires:       go(github.com/mattn/go-sqlite3)
Requires:       go(github.com/mdlayher/netlink)
Requires:       go(github.com/mdlayher/vsock)
Requires:       go(github.com/miekg/dns)
Requires:       go(github.com/mitchellh/mapstructure)
Requires:       go(github.com/moby/docker-image-spec)
Requires:       go(github.com/moby/moby/api)
Requires:       go(github.com/moby/moby/client)
Requires:       go(github.com/moby/sys/mountinfo)
Requires:       go(github.com/modelcontextprotocol/go-sdk)
Requires:       go(github.com/mohae/deepcopy)
Requires:       go(github.com/netsampler/goflow2)
Requires:       go(github.com/oliveagle/jsonpath)
Requires:       go(github.com/open-policy-agent/opa)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/routingconnector)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/spanmetricsconnector)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/loadbalancingexporter)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/datadogextension)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/healthcheckextension)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer/dockerobserver)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer/ecsobserver)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer/hostobserver)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer/k8sobserver)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/pprofextension)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/storage/filestorage)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/datadog)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/resourcetotelemetry)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/attributesprocessor)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/cumulativetodeltaprocessor)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/filterprocessor)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/groupbyattrsprocessor)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/k8sattributesprocessor)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/probabilisticsamplerprocessor)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourceprocessor)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/tailsamplingprocessor)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/transformprocessor)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/filelogreceiver)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/fluentforwardreceiver)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/jaegerreceiver)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sobjectsreceiver)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/prometheusreceiver)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/receivercreator)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/zipkinreceiver)
Requires:       go(github.com/opencontainers/go-digest)
Requires:       go(github.com/opencontainers/image-spec)
Requires:       go(github.com/opencontainers/runtime-spec)
Requires:       go(github.com/openshift/api)
Requires:       go(github.com/outcaste-io/ristretto)
Requires:       go(github.com/pahanini/go-grpc-bidirectional-streaming-example)
Requires:       go(github.com/patrickmn/go-cache)
Requires:       go(github.com/pierrec/lz4/v4)
Requires:       go(github.com/pkg/sftp)
Requires:       go(github.com/planetscale/vtprotobuf)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/prometheus-community/pro-bing)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/prometheus/client_model)
Requires:       go(github.com/prometheus/common)
Requires:       go(github.com/prometheus/procfs)
Requires:       go(github.com/prometheus/prometheus)
Requires:       go(github.com/pulumi/pulumi-aws/sdk/v7)
Requires:       go(github.com/pulumi/pulumi-awsx/sdk/v3)
Requires:       go(github.com/pulumi/pulumi-azure-native-sdk/authorization/v2)
Requires:       go(github.com/pulumi/pulumi-azure-native-sdk/compute/v2)
Requires:       go(github.com/pulumi/pulumi-azure-native-sdk/containerservice/v2)
Requires:       go(github.com/pulumi/pulumi-azure-native-sdk/managedidentity/v2)
Requires:       go(github.com/pulumi/pulumi-azure-native-sdk/network/v2)
Requires:       go(github.com/pulumi/pulumi-azure-native-sdk/v2)
Requires:       go(github.com/pulumi/pulumi-command/sdk)
Requires:       go(github.com/pulumi/pulumi-docker/sdk/v4)
Requires:       go(github.com/pulumi/pulumi-eks/sdk/v4)
Requires:       go(github.com/pulumi/pulumi-gcp/sdk/v7)
Requires:       go(github.com/pulumi/pulumi-kubernetes/sdk/v4)
Requires:       go(github.com/pulumi/pulumi-libvirt/sdk)
Requires:       go(github.com/pulumi/pulumi-random/sdk/v4)
Requires:       go(github.com/pulumi/pulumi-tls/sdk/v4)
Requires:       go(github.com/pulumi/pulumi/sdk/v3)
Requires:       go(github.com/pulumiverse/pulumi-time/sdk)
Requires:       go(github.com/qri-io/jsonpointer)
Requires:       go(github.com/redis/go-redis/v9)
Requires:       go(github.com/richardartoul/molecule)
Requires:       go(github.com/rickar/props)
Requires:       go(github.com/robfig/cron/v3)
Requires:       go(github.com/safchain/ethtool)
Requires:       go(github.com/samber/lo)
Requires:       go(github.com/samuel/go-zookeeper)
Requires:       go(github.com/santhosh-tekuri/jsonschema/v5)
Requires:       go(github.com/santhosh-tekuri/jsonschema/v6)
Requires:       go(github.com/sassoftware/go-rpmutils)
Requires:       go(github.com/shirou/gopsutil/v4)
Requires:       go(github.com/shirou/w32)
Requires:       go(github.com/sijms/go-ora/v2)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(github.com/skydive-project/go-debouncer)
Requires:       go(github.com/smira/go-xz)
Requires:       go(github.com/spf13/afero)
Requires:       go(github.com/spf13/cast)
Requires:       go(github.com/spf13/cobra)
Requires:       go(github.com/spf13/pflag)
Requires:       go(github.com/stormcat24/protodep)
Requires:       go(github.com/streadway/amqp)
Requires:       go(github.com/stretchr/testify)
Requires:       go(github.com/swaggest/jsonschema-go)
Requires:       go(github.com/syndtr/gocapability)
Requires:       go(github.com/tinylib/msgp)
Requires:       go(github.com/twmb/franz-go)
Requires:       go(github.com/twmb/franz-go/pkg/kadm)
Requires:       go(github.com/twmb/murmur3)
Requires:       go(github.com/uber-go/gopatch)
Requires:       go(github.com/uptrace/bun)
Requires:       go(github.com/uptrace/bun/dialect/pgdialect)
Requires:       go(github.com/uptrace/bun/driver/pgdriver)
Requires:       go(github.com/urfave/negroni)
Requires:       go(github.com/vektra/mockery/v3)
Requires:       go(github.com/vibrantbyte/go-antpath)
Requires:       go(github.com/vishvananda/netlink)
Requires:       go(github.com/vishvananda/netns)
Requires:       go(github.com/vmihailenco/msgpack/v5)
Requires:       go(github.com/wI2L/jsondiff)
Requires:       go(github.com/wadey/gocovmerge)
Requires:       go(github.com/weppos/publicsuffix-go)
Requires:       go(github.com/xeipuuv/gojsonschema)
Requires:       go(github.com/xi2/xz)
Requires:       go(github.com/xor-gate/ar)
Requires:       go(github.com/yusufpapurcu/wmi)
Requires:       go(gitlab.com/gitlab-org/api/client-go)
Requires:       go(go.etcd.io/bbolt)
Requires:       go(go.etcd.io/etcd/client/v2)
Requires:       go(go.mongodb.org/mongo-driver)
Requires:       go(go.mongodb.org/mongo-driver/v2)
Requires:       go(go.opentelemetry.io/collector/component)
Requires:       go(go.opentelemetry.io/collector/component/componentstatus)
Requires:       go(go.opentelemetry.io/collector/component/componenttest)
Requires:       go(go.opentelemetry.io/collector/config/confighttp)
Requires:       go(go.opentelemetry.io/collector/config/confignet)
Requires:       go(go.opentelemetry.io/collector/config/configopaque)
Requires:       go(go.opentelemetry.io/collector/config/configoptional)
Requires:       go(go.opentelemetry.io/collector/config/configretry)
Requires:       go(go.opentelemetry.io/collector/config/configtelemetry)
Requires:       go(go.opentelemetry.io/collector/config/configtls)
Requires:       go(go.opentelemetry.io/collector/confmap)
Requires:       go(go.opentelemetry.io/collector/confmap/provider/envprovider)
Requires:       go(go.opentelemetry.io/collector/confmap/provider/fileprovider)
Requires:       go(go.opentelemetry.io/collector/confmap/provider/httpprovider)
Requires:       go(go.opentelemetry.io/collector/confmap/provider/httpsprovider)
Requires:       go(go.opentelemetry.io/collector/confmap/provider/yamlprovider)
Requires:       go(go.opentelemetry.io/collector/confmap/xconfmap)
Requires:       go(go.opentelemetry.io/collector/connector)
Requires:       go(go.opentelemetry.io/collector/consumer)
Requires:       go(go.opentelemetry.io/collector/consumer/xconsumer)
Requires:       go(go.opentelemetry.io/collector/exporter)
Requires:       go(go.opentelemetry.io/collector/exporter/debugexporter)
Requires:       go(go.opentelemetry.io/collector/exporter/exporterhelper)
Requires:       go(go.opentelemetry.io/collector/exporter/nopexporter)
Requires:       go(go.opentelemetry.io/collector/exporter/otlpexporter)
Requires:       go(go.opentelemetry.io/collector/exporter/otlphttpexporter)
Requires:       go(go.opentelemetry.io/collector/extension)
Requires:       go(go.opentelemetry.io/collector/extension/extensioncapabilities)
Requires:       go(go.opentelemetry.io/collector/extension/zpagesextension)
Requires:       go(go.opentelemetry.io/collector/featuregate)
Requires:       go(go.opentelemetry.io/collector/otelcol)
Requires:       go(go.opentelemetry.io/collector/pdata)
Requires:       go(go.opentelemetry.io/collector/pdata/pprofile)
Requires:       go(go.opentelemetry.io/collector/processor)
Requires:       go(go.opentelemetry.io/collector/processor/batchprocessor)
Requires:       go(go.opentelemetry.io/collector/processor/memorylimiterprocessor)
Requires:       go(go.opentelemetry.io/collector/processor/processorhelper)
Requires:       go(go.opentelemetry.io/collector/processor/processorhelper/xprocessorhelper)
Requires:       go(go.opentelemetry.io/collector/processor/xprocessor)
Requires:       go(go.opentelemetry.io/collector/receiver)
Requires:       go(go.opentelemetry.io/collector/receiver/nopreceiver)
Requires:       go(go.opentelemetry.io/collector/receiver/otlpreceiver)
Requires:       go(go.opentelemetry.io/collector/receiver/xreceiver)
Requires:       go(go.opentelemetry.io/collector/service)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/runtime)
Requires:       go(go.opentelemetry.io/ebpf-profiler)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetricgrpc)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/sdk/metric)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(go.temporal.io/api)
Requires:       go(go.temporal.io/sdk)
Requires:       go(go.uber.org/atomic)
Requires:       go(go.uber.org/automaxprocs)
Requires:       go(go.uber.org/dig)
Requires:       go(go.uber.org/fx)
Requires:       go(go.uber.org/multierr)
Requires:       go(go.uber.org/zap)
Requires:       go(go.uber.org/zap/exp)
Requires:       go(go.yaml.in/yaml/v2)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(go4.org/intern)
Requires:       go(go4.org/mem)
Requires:       go(go4.org/netipx)
Requires:       go(golang.org/x/arch)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/exp)
Requires:       go(golang.org/x/mobile)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/perf)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/term)
Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/time)
Requires:       go(golang.org/x/tools)
Requires:       go(golang.org/x/xerrors)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/grpc/cmd/protoc-gen-go-grpc)
Requires:       go(google.golang.org/grpc/examples)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/DataDog/dd-trace-go.v1)
Requires:       go(gopkg.in/evanphx/json-patch.v4)
Requires:       go(gopkg.in/ini.v1)
Requires:       go(gopkg.in/yaml.v3)
Requires:       go(gopkg.in/zorkian/go-datadog-api.v2)
Requires:       go(gotest.tools/gotestsum)
Requires:       go(istio.io/api)
Requires:       go(istio.io/client-go)
Requires:       go(k8s.io/api)
Requires:       go(k8s.io/apiextensions-apiserver)
Requires:       go(k8s.io/apimachinery)
Requires:       go(k8s.io/autoscaler/vertical-pod-autoscaler)
Requires:       go(k8s.io/cli-runtime)
Requires:       go(k8s.io/client-go)
Requires:       go(k8s.io/component-base)
Requires:       go(k8s.io/cri-api)
Requires:       go(k8s.io/cri-client)
Requires:       go(k8s.io/klog/v2)
Requires:       go(k8s.io/kube-aggregator)
Requires:       go(k8s.io/kube-state-metrics/v2)
Requires:       go(k8s.io/kubectl)
Requires:       go(k8s.io/kubelet)
Requires:       go(k8s.io/metrics)
Requires:       go(k8s.io/utils)
Requires:       go(mvdan.cc/sh/v3)
Requires:       go(sigs.k8s.io/custom-metrics-apiserver)
Requires:       go(sigs.k8s.io/gateway-api)
Requires:       go(sigs.k8s.io/karpenter)
Requires:       go(sigs.k8s.io/yaml)

%description
This source package installs the complete Datadog Agent repository, including
its component, telemetry mapping, protocol, trace, and utility Go modules.

%install
# Install each module at its declared import path. Remove nested module
# copies from each parent before installing them at their own paths.
while read -r _source _import _children; do
    _target="%{buildroot}%{go_sys_gopath}/${_import}"
    install -d "${_target}"
    cp -aL "${_source}"/. "${_target}/"
    for _child in ${_children}; do
        rm -rf "${_target}/${_child}"
    done
done <<'GO_MODULES'
. github.com/DataDog/datadog-agent comp/def comp/logs-library internal/tools pkg/api pkg/errors pkg/fips pkg/gohai pkg/metrics pkg/obfuscate pkg/proto pkg/serializer pkg/tagset pkg/template pkg/trace pkg/version test/e2e-framework test/fakeintake test/new-e2e test/otel tools/build-ddot-byoc tools/retry_file_dump comp/core/config comp/core/configsync comp/core/delegatedauth comp/core/status comp/core/telemetry comp/forwarder/defaultforwarder comp/netflow/payload comp/otelcol/logsagentpipeline comp/serializer/logscompression comp/serializer/metricscompression internal/tools/gotest-custom internal/tools/independent-lint internal/tools/modformatter internal/tools/modparser internal/tools/proto internal/tools/worksynchronizer pkg/aggregator/ckey pkg/config/basic pkg/config/buildschema pkg/config/create pkg/config/env pkg/config/helper pkg/config/mock pkg/config/model pkg/config/nodetreemodel pkg/config/remote pkg/config/render_config pkg/config/schema pkg/config/setup pkg/config/structure pkg/config/teeconfig pkg/config/utils pkg/config/viperconfig pkg/fleet/installer pkg/logs/diagnostic pkg/logs/message pkg/logs/sources pkg/logs/types pkg/network/driver pkg/network/payload pkg/networkdevice/profile pkg/networkpath/payload pkg/opentelemetry-mapping-go/inframetadata pkg/orchestrator/model pkg/orchestrator/util pkg/remoteconfig/state pkg/security/secl pkg/security/seclwin pkg/ssi/testutils pkg/status/health pkg/tagger/types pkg/trace/log pkg/trace/otel pkg/trace/stats pkg/trace/traceutil pkg/util/backoff pkg/util/buf pkg/util/cache pkg/util/cgroups pkg/util/common pkg/util/compression pkg/util/defaultpaths pkg/util/executable pkg/util/filesystem pkg/util/flavor pkg/util/fxutil pkg/util/grpc pkg/util/hostinfo pkg/util/hostport pkg/util/http pkg/util/json pkg/util/jsonquery pkg/util/log pkg/util/option pkg/util/otel pkg/util/pointer pkg/util/prometheus pkg/util/quantile pkg/util/scrubber pkg/util/sort pkg/util/startstop pkg/util/statstracker pkg/util/system pkg/util/testutil pkg/util/utilizationtracker pkg/util/uuid pkg/util/winutil comp/anomalydetection/observer/def comp/anomalydetection/recorder/def comp/api/api/def comp/core/agenttelemetry/def comp/core/agenttelemetry/fx comp/core/agenttelemetry/impl comp/core/flare/builder comp/core/flare/types comp/core/hostname/hostnameinterface comp/core/ipc/def comp/core/ipc/httphelpers comp/core/ipc/impl comp/core/ipc/mock comp/core/log/def comp/core/log/fx comp/core/log/impl comp/core/log/impl-trace comp/core/log/mock comp/core/secrets/def comp/core/secrets/fx comp/core/secrets/impl comp/core/secrets/mock comp/core/secrets/noop-impl comp/core/secrets/utils comp/core/status/statusimpl comp/core/tagger/def comp/core/tagger/fx-remote comp/core/tagger/generic_store comp/core/tagger/impl-remote comp/core/tagger/origindetection comp/core/tagger/subscriber comp/core/tagger/tags comp/core/tagger/telemetry comp/core/tagger/types comp/core/tagger/utils comp/forwarder/orchestrator/orchestratorinterface comp/logs/agent/config comp/otelcol/collector-contrib/def comp/otelcol/collector-contrib/impl comp/otelcol/converter/def comp/otelcol/converter/impl comp/otelcol/ddflareextension/def comp/otelcol/ddflareextension/impl comp/otelcol/ddflareextension/types comp/otelcol/ddprofilingextension/def comp/otelcol/ddprofilingextension/impl comp/otelcol/logsagentpipeline/logsagentpipelineimpl comp/otelcol/otlp/testutil comp/otelcol/status/def comp/otelcol/status/impl comp/trace/agent/def comp/trace/compression/def comp/trace/compression/impl-gzip comp/trace/compression/impl-zstd pkg/collector/check/defaults pkg/discovery/tracermetadata/model pkg/dyninst/testprogs/progs pkg/logs/status/statusinterface pkg/logs/status/utils pkg/logs/util/testutils pkg/opentelemetry-mapping-go/otlp/attributes pkg/opentelemetry-mapping-go/otlp/logs pkg/opentelemetry-mapping-go/otlp/metrics pkg/opentelemetry-mapping-go/otlp/rum pkg/process/util/api pkg/util/aws/creds pkg/util/containers/image pkg/util/hostname/validate pkg/util/log/setup pkg/util/quantile/sketchtest comp/otelcol/otlp/components/metricsclient comp/core/delegatedauth/api/cloudauth/aws comp/otelcol/otlp/components/exporter/datadogexporter comp/otelcol/otlp/components/exporter/logsagentexporter comp/otelcol/otlp/components/exporter/serializerexporter comp/otelcol/otlp/components/processor/infraattributesprocessor pkg/opentelemetry-mapping-go/inframetadata/gohai/internal/gohaitest pkg/util/kubernetes/apiserver/common/namespace
comp/def github.com/DataDog/datadog-agent/comp/def
comp/logs-library github.com/DataDog/datadog-agent/comp/logs-library
internal/tools github.com/DataDog/datadog-agent/internal/tools gotest-custom independent-lint modformatter modparser proto worksynchronizer
pkg/api github.com/DataDog/datadog-agent/pkg/api
pkg/errors github.com/DataDog/datadog-agent/pkg/errors
pkg/fips github.com/DataDog/datadog-agent/pkg/fips
pkg/gohai github.com/DataDog/datadog-agent/pkg/gohai
pkg/metrics github.com/DataDog/datadog-agent/pkg/metrics
pkg/obfuscate github.com/DataDog/datadog-agent/pkg/obfuscate
pkg/proto github.com/DataDog/datadog-agent/pkg/proto
pkg/serializer github.com/DataDog/datadog-agent/pkg/serializer
pkg/tagset github.com/DataDog/datadog-agent/pkg/tagset
pkg/template github.com/DataDog/datadog-agent/pkg/template
pkg/trace github.com/DataDog/datadog-agent/pkg/trace log otel stats traceutil
pkg/version github.com/DataDog/datadog-agent/pkg/version
test/e2e-framework github.com/DataDog/datadog-agent/test/e2e-framework
test/fakeintake github.com/DataDog/datadog-agent/test/fakeintake
test/new-e2e github.com/DataDog/datadog-agent/test/new-e2e
test/otel github.com/DataDog/datadog-agent/test/otel
tools/build-ddot-byoc github.com/DataDog/datadog-agent/tools/build-ddot-byoc
tools/retry_file_dump github.com/DataDog/datadog-agent/tools/retry_file_dump
comp/core/config github.com/DataDog/datadog-agent/comp/core/config
comp/core/configsync github.com/DataDog/datadog-agent/comp/core/configsync
comp/core/delegatedauth github.com/DataDog/datadog-agent/comp/core/delegatedauth api/cloudauth/aws
comp/core/status github.com/DataDog/datadog-agent/comp/core/status statusimpl
comp/core/telemetry github.com/DataDog/datadog-agent/comp/core/telemetry
comp/forwarder/defaultforwarder github.com/DataDog/datadog-agent/comp/forwarder/defaultforwarder
comp/netflow/payload github.com/DataDog/datadog-agent/comp/netflow/payload
comp/otelcol/logsagentpipeline github.com/DataDog/datadog-agent/comp/otelcol/logsagentpipeline logsagentpipelineimpl
comp/serializer/logscompression github.com/DataDog/datadog-agent/comp/serializer/logscompression
comp/serializer/metricscompression github.com/DataDog/datadog-agent/comp/serializer/metricscompression
internal/tools/gotest-custom github.com/DataDog/datadog-agent/internal/tools/gotest-custom
internal/tools/independent-lint github.com/DataDog/datadog-agent/internal/tools/independent-lint
internal/tools/modformatter github.com/DataDog/datadog-agent/internal/tools/modformatter
internal/tools/modparser github.com/DataDog/datadog-agent/internal/tools/modparser
internal/tools/proto github.com/DataDog/datadog-agent/internal/tools/proto
internal/tools/worksynchronizer github.com/DataDog/datadog-agent/internal/tools/worksynchronizer
pkg/aggregator/ckey github.com/DataDog/datadog-agent/pkg/aggregator/ckey
pkg/config/basic github.com/DataDog/datadog-agent/pkg/config/basic
pkg/config/buildschema github.com/DataDog/datadog-agent/pkg/config/buildschema
pkg/config/create github.com/DataDog/datadog-agent/pkg/config/create
pkg/config/env github.com/DataDog/datadog-agent/pkg/config/env
pkg/config/helper github.com/DataDog/datadog-agent/pkg/config/helper
pkg/config/mock github.com/DataDog/datadog-agent/pkg/config/mock
pkg/config/model github.com/DataDog/datadog-agent/pkg/config/model
pkg/config/nodetreemodel github.com/DataDog/datadog-agent/pkg/config/nodetreemodel
pkg/config/remote github.com/DataDog/datadog-agent/pkg/config/remote
pkg/config/render_config github.com/DataDog/datadog-agent/pkg/config
pkg/config/schema github.com/DataDog/datadog-agent/pkg/config/schema
pkg/config/setup github.com/DataDog/datadog-agent/pkg/config/setup
pkg/config/structure github.com/DataDog/datadog-agent/pkg/config/structure
pkg/config/teeconfig github.com/DataDog/datadog-agent/pkg/config/teeconfig
pkg/config/utils github.com/DataDog/datadog-agent/pkg/config/utils
pkg/config/viperconfig github.com/DataDog/datadog-agent/pkg/config/viperconfig
pkg/fleet/installer github.com/DataDog/datadog-agent/pkg/fleet/installer
pkg/logs/diagnostic github.com/DataDog/datadog-agent/pkg/logs/diagnostic
pkg/logs/message github.com/DataDog/datadog-agent/pkg/logs/message
pkg/logs/sources github.com/DataDog/datadog-agent/pkg/logs/sources
pkg/logs/types github.com/DataDog/datadog-agent/pkg/logs/types
pkg/network/driver github.com/DataDog/datadog-agent/pkg/network/driver
pkg/network/payload github.com/DataDog/datadog-agent/pkg/network/payload
pkg/networkdevice/profile github.com/DataDog/datadog-agent/pkg/networkdevice/profile
pkg/networkpath/payload github.com/DataDog/datadog-agent/pkg/networkpath/payload
pkg/opentelemetry-mapping-go/inframetadata github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/inframetadata gohai/internal/gohaitest
pkg/orchestrator/model github.com/DataDog/datadog-agent/pkg/orchestrator/model
pkg/orchestrator/util github.com/DataDog/datadog-agent/pkg/orchestrator/util
pkg/remoteconfig/state github.com/DataDog/datadog-agent/pkg/remoteconfig/state
pkg/security/secl github.com/DataDog/datadog-agent/pkg/security/secl
pkg/security/seclwin github.com/DataDog/datadog-agent/pkg/security/seclwin
pkg/ssi/testutils github.com/DataDog/datadog-agent/pkg/ssi/testutils
pkg/status/health github.com/DataDog/datadog-agent/pkg/status/health
pkg/tagger/types github.com/DataDog/datadog-agent/pkg/tagger/types
pkg/trace/log github.com/DataDog/datadog-agent/pkg/trace/log
pkg/trace/otel github.com/DataDog/datadog-agent/pkg/trace/otel
pkg/trace/stats github.com/DataDog/datadog-agent/pkg/trace/stats
pkg/trace/traceutil github.com/DataDog/datadog-agent/pkg/trace/traceutil
pkg/util/backoff github.com/DataDog/datadog-agent/pkg/util/backoff
pkg/util/buf github.com/DataDog/datadog-agent/pkg/util/buf
pkg/util/cache github.com/DataDog/datadog-agent/pkg/util/cache
pkg/util/cgroups github.com/DataDog/datadog-agent/pkg/util/cgroups
pkg/util/common github.com/DataDog/datadog-agent/pkg/util/common
pkg/util/compression github.com/DataDog/datadog-agent/pkg/util/compression
pkg/util/defaultpaths github.com/DataDog/datadog-agent/pkg/util/defaultpaths
pkg/util/executable github.com/DataDog/datadog-agent/pkg/util/executable
pkg/util/filesystem github.com/DataDog/datadog-agent/pkg/util/filesystem
pkg/util/flavor github.com/DataDog/datadog-agent/pkg/util/flavor
pkg/util/fxutil github.com/DataDog/datadog-agent/pkg/util/fxutil
pkg/util/grpc github.com/DataDog/datadog-agent/pkg/util/grpc
pkg/util/hostinfo github.com/DataDog/datadog-agent/pkg/util/hostinfo
pkg/util/hostport github.com/DataDog/datadog-agent/pkg/util/hostport
pkg/util/http github.com/DataDog/datadog-agent/pkg/util/http
pkg/util/json github.com/DataDog/datadog-agent/pkg/util/json
pkg/util/jsonquery github.com/DataDog/datadog-agent/pkg/util/jsonquery
pkg/util/log github.com/DataDog/datadog-agent/pkg/util/log setup
pkg/util/option github.com/DataDog/datadog-agent/pkg/util/option
pkg/util/otel github.com/DataDog/datadog-agent/pkg/util/otel
pkg/util/pointer github.com/DataDog/datadog-agent/pkg/util/pointer
pkg/util/prometheus github.com/DataDog/datadog-agent/pkg/util/prometheus
pkg/util/quantile github.com/DataDog/datadog-agent/pkg/util/quantile sketchtest
pkg/util/scrubber github.com/DataDog/datadog-agent/pkg/util/scrubber
pkg/util/sort github.com/DataDog/datadog-agent/pkg/util/sort
pkg/util/startstop github.com/DataDog/datadog-agent/pkg/util/startstop
pkg/util/statstracker github.com/DataDog/datadog-agent/pkg/util/statstracker
pkg/util/system github.com/DataDog/datadog-agent/pkg/util/system
pkg/util/testutil github.com/DataDog/datadog-agent/pkg/util/testutil
pkg/util/utilizationtracker github.com/DataDog/datadog-agent/pkg/util/utilizationtracker
pkg/util/uuid github.com/DataDog/datadog-agent/pkg/util/uuid
pkg/util/winutil github.com/DataDog/datadog-agent/pkg/util/winutil
comp/anomalydetection/observer/def github.com/DataDog/datadog-agent/comp/anomalydetection/observer/def
comp/anomalydetection/recorder/def github.com/DataDog/datadog-agent/comp/anomalydetection/recorder/def
comp/api/api/def github.com/DataDog/datadog-agent/comp/api/api/def
comp/core/agenttelemetry/def github.com/DataDog/datadog-agent/comp/core/agenttelemetry/def
comp/core/agenttelemetry/fx github.com/DataDog/datadog-agent/comp/core/agenttelemetry/fx
comp/core/agenttelemetry/impl github.com/DataDog/datadog-agent/comp/core/agenttelemetry/impl
comp/core/flare/builder github.com/DataDog/datadog-agent/comp/core/flare/builder
comp/core/flare/types github.com/DataDog/datadog-agent/comp/core/flare/types
comp/core/hostname/hostnameinterface github.com/DataDog/datadog-agent/comp/core/hostname/hostnameinterface
comp/core/ipc/def github.com/DataDog/datadog-agent/comp/core/ipc/def
comp/core/ipc/httphelpers github.com/DataDog/datadog-agent/comp/core/ipc/httphelpers
comp/core/ipc/impl github.com/DataDog/datadog-agent/comp/core/ipc/impl
comp/core/ipc/mock github.com/DataDog/datadog-agent/comp/core/ipc/mock
comp/core/log/def github.com/DataDog/datadog-agent/comp/core/log/def
comp/core/log/fx github.com/DataDog/datadog-agent/comp/core/log/fx
comp/core/log/impl github.com/DataDog/datadog-agent/comp/core/log/impl
comp/core/log/impl-trace github.com/DataDog/datadog-agent/comp/core/log/impl-trace
comp/core/log/mock github.com/DataDog/datadog-agent/comp/core/log/mock
comp/core/secrets/def github.com/DataDog/datadog-agent/comp/core/secrets/def
comp/core/secrets/fx github.com/DataDog/datadog-agent/comp/core/secrets/fx
comp/core/secrets/impl github.com/DataDog/datadog-agent/comp/core/secrets/impl
comp/core/secrets/mock github.com/DataDog/datadog-agent/comp/core/secrets/mock
comp/core/secrets/noop-impl github.com/DataDog/datadog-agent/comp/core/secrets/noop-impl
comp/core/secrets/utils github.com/DataDog/datadog-agent/comp/core/secrets/utils
comp/core/status/statusimpl github.com/DataDog/datadog-agent/comp/core/status/statusimpl
comp/core/tagger/def github.com/DataDog/datadog-agent/comp/core/tagger/def
comp/core/tagger/fx-remote github.com/DataDog/datadog-agent/comp/core/tagger/fx-remote
comp/core/tagger/generic_store github.com/DataDog/datadog-agent/comp/core/tagger/generic_store
comp/core/tagger/impl-remote github.com/DataDog/datadog-agent/comp/core/tagger/impl-remote
comp/core/tagger/origindetection github.com/DataDog/datadog-agent/comp/core/tagger/origindetection
comp/core/tagger/subscriber github.com/DataDog/datadog-agent/comp/core/tagger/subscriber
comp/core/tagger/tags github.com/DataDog/datadog-agent/comp/core/tagger/tags
comp/core/tagger/telemetry github.com/DataDog/datadog-agent/comp/core/tagger/telemetry
comp/core/tagger/types github.com/DataDog/datadog-agent/comp/core/tagger/types
comp/core/tagger/utils github.com/DataDog/datadog-agent/comp/core/tagger/utils
comp/forwarder/orchestrator/orchestratorinterface github.com/DataDog/datadog-agent/comp/forwarder/orchestrator/orchestratorinterface
comp/logs/agent/config github.com/DataDog/datadog-agent/comp/logs/agent/config
comp/otelcol/collector-contrib/def github.com/DataDog/datadog-agent/comp/otelcol/collector-contrib/def
comp/otelcol/collector-contrib/impl github.com/DataDog/datadog-agent/comp/otelcol/collector-contrib/impl
comp/otelcol/converter/def github.com/DataDog/datadog-agent/comp/otelcol/converter/def
comp/otelcol/converter/impl github.com/DataDog/datadog-agent/comp/otelcol/converter/impl
comp/otelcol/ddflareextension/def github.com/DataDog/datadog-agent/comp/otelcol/ddflareextension/def
comp/otelcol/ddflareextension/impl github.com/DataDog/datadog-agent/comp/otelcol/ddflareextension/impl
comp/otelcol/ddflareextension/types github.com/DataDog/datadog-agent/comp/otelcol/ddflareextension/types
comp/otelcol/ddprofilingextension/def github.com/DataDog/datadog-agent/comp/otelcol/ddprofilingextension/def
comp/otelcol/ddprofilingextension/impl github.com/DataDog/datadog-agent/comp/otelcol/ddprofilingextension/impl
comp/otelcol/logsagentpipeline/logsagentpipelineimpl github.com/DataDog/datadog-agent/comp/otelcol/logsagentpipeline/logsagentpipelineimpl
comp/otelcol/otlp/testutil github.com/DataDog/datadog-agent/comp/otelcol/otlp/testutil
comp/otelcol/status/def github.com/DataDog/datadog-agent/comp/otelcol/status/def
comp/otelcol/status/impl github.com/DataDog/datadog-agent/comp/otelcol/status/impl
comp/trace/agent/def github.com/DataDog/datadog-agent/comp/trace/agent/def
comp/trace/compression/def github.com/DataDog/datadog-agent/comp/trace/compression/def
comp/trace/compression/impl-gzip github.com/DataDog/datadog-agent/comp/trace/compression/impl-gzip
comp/trace/compression/impl-zstd github.com/DataDog/datadog-agent/comp/trace/compression/impl-zstd
pkg/collector/check/defaults github.com/DataDog/datadog-agent/pkg/collector/check/defaults
pkg/discovery/tracermetadata/model github.com/DataDog/datadog-agent/pkg/discovery/tracermetadata/model
pkg/dyninst/testprogs/progs github.com/DataDog/datadog-agent/pkg/dyninst/testprogs/progs
pkg/logs/status/statusinterface github.com/DataDog/datadog-agent/pkg/logs/status/statusinterface
pkg/logs/status/utils github.com/DataDog/datadog-agent/pkg/logs/status/utils
pkg/logs/util/testutils github.com/DataDog/datadog-agent/pkg/logs/util/testutils
pkg/opentelemetry-mapping-go/otlp/attributes github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/attributes
pkg/opentelemetry-mapping-go/otlp/logs github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/logs
pkg/opentelemetry-mapping-go/otlp/metrics github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/metrics
pkg/opentelemetry-mapping-go/otlp/rum github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/rum
pkg/process/util/api github.com/DataDog/datadog-agent/pkg/process/util/api
pkg/util/aws/creds github.com/DataDog/datadog-agent/pkg/util/aws/creds
pkg/util/containers/image github.com/DataDog/datadog-agent/pkg/util/containers/image
pkg/util/hostname/validate github.com/DataDog/datadog-agent/pkg/util/hostname/validate
pkg/util/log/setup github.com/DataDog/datadog-agent/pkg/util/log/setup
pkg/util/quantile/sketchtest github.com/DataDog/datadog-agent/pkg/util/quantile/sketchtest
comp/otelcol/otlp/components/metricsclient github.com/DataDog/datadog-agent/comp/otelcol/otlp/components/metricsclient
comp/core/delegatedauth/api/cloudauth/aws github.com/DataDog/datadog-agent/comp/core/delegatedauth/api/cloudauth/aws
comp/otelcol/otlp/components/exporter/datadogexporter github.com/DataDog/datadog-agent/comp/otelcol/otlp/components/exporter/datadogexporter
comp/otelcol/otlp/components/exporter/logsagentexporter github.com/DataDog/datadog-agent/comp/otelcol/otlp/components/exporter/logsagentexporter
comp/otelcol/otlp/components/exporter/serializerexporter github.com/DataDog/datadog-agent/comp/otelcol/otlp/components/exporter/serializerexporter
comp/otelcol/otlp/components/processor/infraattributesprocessor github.com/DataDog/datadog-agent/comp/otelcol/otlp/components/processor/infraattributesprocessor
pkg/opentelemetry-mapping-go/inframetadata/gohai/internal/gohaitest github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/inframetadata/gohai/internal/gohaitest
pkg/util/kubernetes/apiserver/common/namespace github.com/DataDog/datadog-agent/pkg/util/kubernetes/apiserver/common/namespace
GO_MODULES

# Architecture-specific binaries are test fixtures, not Go source artifacts.
find "%{buildroot}%{go_sys_gopath}/%{go_import_path}" -type f \
    \( -name '*.so' -o -name '*.dll' -o -name '*.o' -o -name '*.exe' \) \
    -delete
rm -f "%{buildroot}%{go_sys_gopath}/%{go_import_path}"/pkg/network/usm/testdata/site-packages/ddtrace/libssl.so.*
find "%{buildroot}%{go_sys_gopath}/%{go_import_path}" -type f -exec chmod a-x {} +

%check
%go_common
# Test the installed layout, including nested modules, without loading a
# second copy of the repository or using the system's older source package.
install -d "%{_builddir}/go/src"
cp -a "%{buildroot}%{go_sys_gopath}/." "%{_builddir}/go/src/"
_go_packages=$(go list -e -f '{{.ImportPath}}' github.com/DataDog/datadog-agent/...)
_go_packages=$(printf '%s\n' "${_go_packages}" | sort -u)
_go_tests=
set -f
for _package in ${_go_packages}; do
    _skip=0
    for _exclude in %{?go_test_exclude}; do
        if [ "${_package}" = "${_exclude}" ]; then _skip=1; fi
    done
    for _exclude in %{?go_test_exclude_glob}; do
        case "${_package}" in ${_exclude}) _skip=1 ;; esac
    done
    [ "${_skip}" -eq 1 ] || _go_tests="${_go_tests} ${_package}"
done
set +f
test -n "${_go_tests}"
go test %{go_test_flags_default} ${_go_tests}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
