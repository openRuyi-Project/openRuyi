# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           opentelemetry-operations-go
%define go_import_path  github.com/GoogleCloudPlatform/opentelemetry-operations-go

Name:           go-github-googlecloudplatform-opentelemetry-operations-go
Version:        0.62.0
Release:        %autorelease
Summary:        Google Cloud integrations for OpenTelemetry
License:        Apache-2.0
URL:            https://github.com/GoogleCloudPlatform/opentelemetry-operations-go
#!RemoteAsset:  sha256:a6fae3974bd416025cc469762db31ab707818b4674b9d93336f13805b03cd2e8
Source0:        https://github.com/GoogleCloudPlatform/opentelemetry-operations-go/archive/refs/tags/exporter/metric/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# GitHub includes the nested release tag in the archive directory name.
BuildOption(prep):  -n %{_name}-exporter-metric-v%{version}

BuildRequires:  go
BuildRequires:  go(4d63.com/gocheckcompilerdirectives)
BuildRequires:  go(4d63.com/gochecknoglobals)
BuildRequires:  go(charm.land/lipgloss/v2)
BuildRequires:  go(cloud.google.com/go)
BuildRequires:  go(cloud.google.com/go/auth)
BuildRequires:  go(cloud.google.com/go/auth/oauth2adapt)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(cloud.google.com/go/functions)
BuildRequires:  go(cloud.google.com/go/iam)
BuildRequires:  go(cloud.google.com/go/logging)
BuildRequires:  go(cloud.google.com/go/longrunning)
BuildRequires:  go(cloud.google.com/go/monitoring)
BuildRequires:  go(cloud.google.com/go/pubsub/v2)
BuildRequires:  go(cloud.google.com/go/trace)
BuildRequires:  go(codeberg.org/chavacava/garif)
BuildRequires:  go(codeberg.org/polyfloyd/go-errorlint)
BuildRequires:  go(dev.gaijin.team/go/exhaustruct/v4)
BuildRequires:  go(dev.gaijin.team/go/exhaustruct/v5)
BuildRequires:  go(dev.gaijin.team/go/golib)
BuildRequires:  go(github.com/4meepo/tagalign)
BuildRequires:  go(github.com/Abirdcfly/dupword)
BuildRequires:  go(github.com/AdminBenni/iota-mixing)
BuildRequires:  go(github.com/AlwxSin/noinlineerr)
BuildRequires:  go(github.com/Antonboom/errname)
BuildRequires:  go(github.com/Antonboom/nilnil)
BuildRequires:  go(github.com/Antonboom/testifylint)
BuildRequires:  go(github.com/BurntSushi/toml)
BuildRequires:  go(github.com/ClickHouse/clickhouse-go-linter)
BuildRequires:  go(github.com/Djarvur/go-err113)
BuildRequires:  go(github.com/GoogleCloudPlatform/functions-framework-go)
BuildRequires:  go(github.com/Masterminds/semver/v3)
BuildRequires:  go(github.com/MirrexOne/unqueryvet)
BuildRequires:  go(github.com/OpenPeeDeeP/depguard/v2)
BuildRequires:  go(github.com/alecthomas/chroma/v2)
BuildRequires:  go(github.com/alecthomas/go-check-sumtype)
BuildRequires:  go(github.com/alexkohler/nakedret/v2)
BuildRequires:  go(github.com/alexkohler/prealloc)
BuildRequires:  go(github.com/alfatraining/structtag)
BuildRequires:  go(github.com/alingse/asasalint)
BuildRequires:  go(github.com/alingse/nilnesserr)
BuildRequires:  go(github.com/ashanbrown/forbidigo/v2)
BuildRequires:  go(github.com/ashanbrown/makezero/v2)
BuildRequires:  go(github.com/beorn7/perks)
BuildRequires:  go(github.com/bkielbasa/cyclop)
BuildRequires:  go(github.com/blizzy78/varnamelen)
BuildRequires:  go(github.com/bombsimon/wsl/v4)
BuildRequires:  go(github.com/bombsimon/wsl/v5)
BuildRequires:  go(github.com/breml/bidichk)
BuildRequires:  go(github.com/breml/errchkjson)
BuildRequires:  go(github.com/butuzov/ireturn)
BuildRequires:  go(github.com/butuzov/mirror)
BuildRequires:  go(github.com/catenacyber/perfsprint)
BuildRequires:  go(github.com/ccojocar/zxcvbn-go)
BuildRequires:  go(github.com/cenkalti/backoff/v5)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/charithe/durationcheck)
BuildRequires:  go(github.com/charmbracelet/colorprofile)
BuildRequires:  go(github.com/charmbracelet/ultraviolet)
BuildRequires:  go(github.com/charmbracelet/x/ansi)
BuildRequires:  go(github.com/charmbracelet/x/term)
BuildRequires:  go(github.com/charmbracelet/x/termios)
BuildRequires:  go(github.com/charmbracelet/x/windows)
BuildRequires:  go(github.com/ckaznocha/intrange)
BuildRequires:  go(github.com/client9/misspell)
BuildRequires:  go(github.com/clipperhouse/displaywidth)
BuildRequires:  go(github.com/clipperhouse/uax29/v2)
BuildRequires:  go(github.com/cloudevents/sdk-go/v2)
BuildRequires:  go(github.com/curioswitch/go-reassign)
BuildRequires:  go(github.com/daixiang0/gci)
BuildRequires:  go(github.com/dave/dst)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/denis-tingaikin/go-header)
BuildRequires:  go(github.com/dlclark/regexp2/v2)
BuildRequires:  go(github.com/ebitengine/purego)
BuildRequires:  go(github.com/ettle/strcase)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/fatih/structtag)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/firefart/nonamedreturns)
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/fzipp/gocyclo)
BuildRequires:  go(github.com/ghostiam/protogetter)
BuildRequires:  go(github.com/go-critic/go-critic)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/go-ole/go-ole)
BuildRequires:  go(github.com/go-toolsmith/astcast)
BuildRequires:  go(github.com/go-toolsmith/astcopy)
BuildRequires:  go(github.com/go-toolsmith/astequal)
BuildRequires:  go(github.com/go-toolsmith/astfmt)
BuildRequires:  go(github.com/go-toolsmith/astp)
BuildRequires:  go(github.com/go-toolsmith/strparse)
BuildRequires:  go(github.com/go-toolsmith/typep)
BuildRequires:  go(github.com/go-viper/mapstructure/v2)
BuildRequires:  go(github.com/go-xmlfmt/xmlfmt)
BuildRequires:  go(github.com/gobwas/glob)
BuildRequires:  go(github.com/godoc-lint/godoc-lint)
BuildRequires:  go(github.com/gofrs/flock)
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
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/s2a-go)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(github.com/gordonklaus/ineffassign)
BuildRequires:  go(github.com/gostaticanalysis/analysisutil)
BuildRequires:  go(github.com/gostaticanalysis/comment)
BuildRequires:  go(github.com/gostaticanalysis/forcetypeassert)
BuildRequires:  go(github.com/gostaticanalysis/nilerr)
BuildRequires:  go(github.com/grpc-ecosystem/grpc-gateway/v2)
BuildRequires:  go(github.com/hashicorp/go-immutable-radix/v2)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/hashicorp/golang-lru/v2)
BuildRequires:  go(github.com/hashicorp/hcl)
BuildRequires:  go(github.com/hexops/gotextdiff)
BuildRequires:  go(github.com/inconshreveable/mousetrap)
BuildRequires:  go(github.com/itchyny/go-yaml)
BuildRequires:  go(github.com/itchyny/gojq)
BuildRequires:  go(github.com/itchyny/timefmt-go)
BuildRequires:  go(github.com/jgautheron/goconst)
BuildRequires:  go(github.com/jjti/go-spancheck)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/julz/importas)
BuildRequires:  go(github.com/karamaru-alpha/copyloopvar)
BuildRequires:  go(github.com/kisielk/errcheck)
BuildRequires:  go(github.com/kkHAIKE/contextcheck)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/knadh/koanf/maps)
BuildRequires:  go(github.com/knadh/koanf/providers/confmap)
BuildRequires:  go(github.com/knadh/koanf/v2)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/kulti/thelper)
BuildRequires:  go(github.com/kunwardeep/paralleltest)
BuildRequires:  go(github.com/lasiar/canonicalheader)
BuildRequires:  go(github.com/ldez/exptostd)
BuildRequires:  go(github.com/ldez/gomoddirectives)
BuildRequires:  go(github.com/ldez/grignotin)
BuildRequires:  go(github.com/ldez/structtags)
BuildRequires:  go(github.com/ldez/tagliatelle)
BuildRequires:  go(github.com/ldez/usetesting)
BuildRequires:  go(github.com/leonklingele/grouper)
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)
BuildRequires:  go(github.com/lufia/plan9stats)
BuildRequires:  go(github.com/macabu/inamedparam)
BuildRequires:  go(github.com/magiconair/properties)
BuildRequires:  go(github.com/manuelarte/embeddedstructfieldcheck)
BuildRequires:  go(github.com/manuelarte/funcorder)
BuildRequires:  go(github.com/maratori/testableexamples)
BuildRequires:  go(github.com/maratori/testpackage)
BuildRequires:  go(github.com/matoous/godox)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/mgechev/revive)
BuildRequires:  go(github.com/mitchellh/copystructure)
BuildRequires:  go(github.com/mitchellh/go-homedir)
BuildRequires:  go(github.com/mitchellh/mapstructure)
BuildRequires:  go(github.com/mitchellh/reflectwalk)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/moricho/tparallel)
BuildRequires:  go(github.com/muesli/cancelreader)
BuildRequires:  go(github.com/munnerz/goautoneg)
BuildRequires:  go(github.com/nakabonne/nestif)
BuildRequires:  go(github.com/nishanths/exhaustive)
BuildRequires:  go(github.com/nishanths/predeclared)
BuildRequires:  go(github.com/nunnatsa/ginkgolinter)
BuildRequires:  go(github.com/pelletier/go-toml/v2)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/power-devops/perfstat)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/otlptranslator)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(github.com/quasilyte/go-ruleguard)
BuildRequires:  go(github.com/quasilyte/go-ruleguard/dsl)
BuildRequires:  go(github.com/quasilyte/gogrep)
BuildRequires:  go(github.com/quasilyte/regex/syntax)
BuildRequires:  go(github.com/quasilyte/stdinfo)
BuildRequires:  go(github.com/raeperd/recvcheck)
BuildRequires:  go(github.com/rivo/uniseg)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/ryancurrah/gomodguard)
BuildRequires:  go(github.com/ryancurrah/gomodguard/v2)
BuildRequires:  go(github.com/ryanrolds/sqlclosecheck)
BuildRequires:  go(github.com/sagikazarmark/locafero)
BuildRequires:  go(github.com/sagikazarmark/slog-shim)
BuildRequires:  go(github.com/sanposhiho/wastedassign/v2)
BuildRequires:  go(github.com/santhosh-tekuri/jsonschema/v6)
BuildRequires:  go(github.com/sashamelentyev/interfacebloat)
BuildRequires:  go(github.com/sashamelentyev/usestdlibvars)
BuildRequires:  go(github.com/securego/gosec/v2)
BuildRequires:  go(github.com/shirou/gopsutil/v4)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/sivchari/containedctx)
BuildRequires:  go(github.com/sonatard/noctx)
BuildRequires:  go(github.com/sourcegraph/conc)
BuildRequires:  go(github.com/sourcegraph/go-diff)
BuildRequires:  go(github.com/spf13/afero)
BuildRequires:  go(github.com/spf13/cast)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/spf13/viper)
BuildRequires:  go(github.com/ssgreg/nlreturn/v2)
BuildRequires:  go(github.com/stbenjam/no-sprintf-host-port)
BuildRequires:  go(github.com/stretchr/objx)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/subosito/gotenv)
BuildRequires:  go(github.com/tetafro/godot)
BuildRequires:  go(github.com/tidwall/gjson)
BuildRequires:  go(github.com/tidwall/match)
BuildRequires:  go(github.com/tidwall/pretty)
BuildRequires:  go(github.com/tidwall/tinylru)
BuildRequires:  go(github.com/tidwall/wal)
BuildRequires:  go(github.com/timakin/bodyclose)
BuildRequires:  go(github.com/timonwong/loggercheck)
BuildRequires:  go(github.com/tklauser/go-sysconf)
BuildRequires:  go(github.com/tklauser/numcpus)
BuildRequires:  go(github.com/tomarrell/wrapcheck/v2)
BuildRequires:  go(github.com/tommy-muehle/go-mnd/v2)
BuildRequires:  go(github.com/ultraware/funlen)
BuildRequires:  go(github.com/ultraware/whitespace)
BuildRequires:  go(github.com/uudashr/gocognit)
BuildRequires:  go(github.com/uudashr/iface)
BuildRequires:  go(github.com/wadey/gocovmerge)
BuildRequires:  go(github.com/xen0n/gosmopolitan)
BuildRequires:  go(github.com/xo/terminfo)
BuildRequires:  go(github.com/yagipy/maintidx)
BuildRequires:  go(github.com/yeya24/promlinter)
BuildRequires:  go(github.com/ykadowak/zerologlint)
BuildRequires:  go(github.com/yusufpapurcu/wmi)
BuildRequires:  go(gitlab.com/bosi/decorder)
BuildRequires:  go(go-simpler.org/musttag)
BuildRequires:  go(go-simpler.org/sloglint)
BuildRequires:  go(go.augendre.info/arangolint)
BuildRequires:  go(go.augendre.info/fatcontext)
BuildRequires:  go(go.opencensus.io)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/collector/component)
BuildRequires:  go(go.opentelemetry.io/collector/component/componentstatus)
BuildRequires:  go(go.opentelemetry.io/collector/component/componenttest)
BuildRequires:  go(go.opentelemetry.io/collector/config/configtelemetry)
BuildRequires:  go(go.opentelemetry.io/collector/confmap)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/provider/envprovider)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/provider/fileprovider)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/provider/httpprovider)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/provider/yamlprovider)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/xconfmap)
BuildRequires:  go(go.opentelemetry.io/collector/connector)
BuildRequires:  go(go.opentelemetry.io/collector/connector/connectortest)
BuildRequires:  go(go.opentelemetry.io/collector/connector/xconnector)
BuildRequires:  go(go.opentelemetry.io/collector/consumer)
BuildRequires:  go(go.opentelemetry.io/collector/consumer/consumererror)
BuildRequires:  go(go.opentelemetry.io/collector/consumer/consumertest)
BuildRequires:  go(go.opentelemetry.io/collector/consumer/xconsumer)
BuildRequires:  go(go.opentelemetry.io/collector/exporter)
BuildRequires:  go(go.opentelemetry.io/collector/exporter/exportertest)
BuildRequires:  go(go.opentelemetry.io/collector/exporter/xexporter)
BuildRequires:  go(go.opentelemetry.io/collector/extension)
BuildRequires:  go(go.opentelemetry.io/collector/extension/extensionauth)
BuildRequires:  go(go.opentelemetry.io/collector/extension/extensioncapabilities)
BuildRequires:  go(go.opentelemetry.io/collector/extension/extensiontest)
BuildRequires:  go(go.opentelemetry.io/collector/featuregate)
BuildRequires:  go(go.opentelemetry.io/collector/internal/componentalias)
BuildRequires:  go(go.opentelemetry.io/collector/internal/fanoutconsumer)
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
BuildRequires:  go(go.opentelemetry.io/collector/processor/processortest)
BuildRequires:  go(go.opentelemetry.io/collector/processor/xprocessor)
BuildRequires:  go(go.opentelemetry.io/collector/receiver)
BuildRequires:  go(go.opentelemetry.io/collector/receiver/receivertest)
BuildRequires:  go(go.opentelemetry.io/collector/receiver/xreceiver)
BuildRequires:  go(go.opentelemetry.io/collector/service)
BuildRequires:  go(go.opentelemetry.io/collector/service/hostcapabilities)
BuildRequires:  go(go.opentelemetry.io/contrib)
BuildRequires:  go(go.opentelemetry.io/contrib/bridges/otelslog)
BuildRequires:  go(go.opentelemetry.io/contrib/detectors/gcp)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
BuildRequires:  go(go.opentelemetry.io/contrib/otelconf)
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
BuildRequires:  go(go.uber.org/atomic)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/exp/typeparams)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/telemetry)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/vuln)
BuildRequires:  go(gonum.org/v1/gonum)
BuildRequires:  go(google.golang.org/api)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/ini.v1)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(honnef.co/go/tools)
BuildRequires:  go(mvdan.cc/gofumpt)
BuildRequires:  go(mvdan.cc/unparam)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/e2e-test-server) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/e2e-test-server/cloudfunctions) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/e2e-test-server/endtoendserver) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/e2e-test-server/scenarios) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/example/log/slogbridge) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/example/metric/collector) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/example/metric/exponential_histogram) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/example/metric/otlpgrpc) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/example/metric/sdk) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/example/trace/http) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/example/trace/otlpgrpc) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/example/trace/otlphttp) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector/googlemanagedprometheus) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector/integrationtest) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector/integrationtest/protos) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector/integrationtest/testcases) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector/internal/datapointstorage) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector/internal/logsutil) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector/internal/normalization) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/trace) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/extension/googleclientauthextension) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/cloudmock) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/propagator) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/tools) = %{version}

Requires:       go(cloud.google.com/go/auth)
Requires:       go(cloud.google.com/go/compute/metadata)
Requires:       go(cloud.google.com/go/logging)
Requires:       go(cloud.google.com/go/monitoring)
Requires:       go(cloud.google.com/go/pubsub/v2)
Requires:       go(cloud.google.com/go/trace)
Requires:       go(github.com/GoogleCloudPlatform/functions-framework-go)
Requires:       go(github.com/client9/misspell)
Requires:       go(github.com/cloudevents/sdk-go/v2)
Requires:       go(github.com/fsnotify/fsnotify)
Requires:       go(github.com/go-viper/mapstructure/v2)
Requires:       go(github.com/golangci/golangci-lint/v2)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/googleapis/gax-go/v2)
Requires:       go(github.com/itchyny/gojq)
Requires:       go(github.com/prometheus/common)
Requires:       go(github.com/prometheus/otlptranslator)
Requires:       go(github.com/stretchr/testify)
Requires:       go(github.com/tidwall/wal)
Requires:       go(github.com/wadey/gocovmerge)
Requires:       go(go.opentelemetry.io/collector/component)
Requires:       go(go.opentelemetry.io/collector/component/componenttest)
Requires:       go(go.opentelemetry.io/collector/exporter)
Requires:       go(go.opentelemetry.io/collector/extension)
Requires:       go(go.opentelemetry.io/collector/extension/extensionauth)
Requires:       go(go.opentelemetry.io/collector/featuregate)
Requires:       go(go.opentelemetry.io/collector/pdata)
Requires:       go(go.opentelemetry.io/contrib/bridges/otelslog)
Requires:       go(go.opentelemetry.io/contrib/detectors/gcp)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploghttp)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetricgrpc)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp)
Requires:       go(go.opentelemetry.io/otel/exporters/stdout/stdoutlog)
Requires:       go(go.opentelemetry.io/otel/log)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/sdk)
Requires:       go(go.opentelemetry.io/otel/sdk/log)
Requires:       go(go.opentelemetry.io/otel/sdk/metric)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(go.uber.org/atomic)
Requires:       go(go.uber.org/zap)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/tools)
Requires:       go(golang.org/x/vuln)
Requires:       go(gonum.org/v1/gonum)
Requires:       go(google.golang.org/api)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/genproto/googleapis/api)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

# Replace the former source RPMs because this repository owns their paths.
Obsoletes:      go-github-googlecloudplatform-opentelemetry-operations-go-detectors-gcp
Obsoletes:      go-github-googlecloudplatform-opentelemetry-operations-go-exporter-metric
Obsoletes:      go-github-googlecloudplatform-opentelemetry-operations-go-internal-cloudmock
Obsoletes:      go-github-googlecloudplatform-opentelemetry-operations-go-internal-resourcemapping

%description
This package provides the complete Google Cloud OpenTelemetry integration
repository, including detectors, exporters, propagators, and test support.

%install
# All published modules share the repository root import prefix, so the
# standard macro preserves the complete source tree and nested go.mod files.
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
        github.com/GoogleCloudPlatform/opentelemetry-operations-go|github.com/GoogleCloudPlatform/opentelemetry-operations-go/*) ;;
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
