# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           etcd
%define go_import_path  go.etcd.io/etcd

Name:           go-etcd-io-etcd
Version:        3.7.1
Release:        %autorelease
Summary:        Go API, client, and server modules for etcd
License:        Apache-2.0
URL:            https://github.com/etcd-io/etcd
#!RemoteAsset:  sha256:95352a96ffb1d92df77b5bce2bb239046fa94cd99dc839ff7eecfdc983416637
Source0:        https://github.com/etcd-io/etcd/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(4d63.com/gocheckcompilerdirectives)
BuildRequires:  go(4d63.com/gochecknoglobals)
BuildRequires:  go(charm.land/lipgloss/v2)
BuildRequires:  go(codeberg.org/chavacava/garif)
BuildRequires:  go(codeberg.org/go-fonts/liberation)
BuildRequires:  go(codeberg.org/go-latex/latex)
BuildRequires:  go(codeberg.org/go-pdf/fpdf)
BuildRequires:  go(codeberg.org/polyfloyd/go-errorlint)
BuildRequires:  go(dev.gaijin.team/go/exhaustruct/v4)
BuildRequires:  go(dev.gaijin.team/go/golib)
BuildRequires:  go(filippo.io/edwards25519)
BuildRequires:  go(git.sr.ht/~sbinet/gg)
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
BuildRequires:  go(github.com/GoogleCloudPlatform/testgrid)
BuildRequires:  go(github.com/Masterminds/semver/v3)
BuildRequires:  go(github.com/MirrexOne/unqueryvet)
BuildRequires:  go(github.com/OpenPeeDeeP/depguard/v2)
BuildRequires:  go(github.com/VividCortex/ewma)
BuildRequires:  go(github.com/ajstarks/svgo)
BuildRequires:  go(github.com/alecthomas/chroma/v2)
BuildRequires:  go(github.com/alecthomas/go-check-sumtype)
BuildRequires:  go(github.com/alexfalkowski/gocovmerge)
BuildRequires:  go(github.com/alexkohler/nakedret/v2)
BuildRequires:  go(github.com/alexkohler/prealloc)
BuildRequires:  go(github.com/alfatraining/structtag)
BuildRequires:  go(github.com/alingse/asasalint)
BuildRequires:  go(github.com/alingse/nilnesserr)
BuildRequires:  go(github.com/anishathalye/porcupine)
BuildRequires:  go(github.com/antithesishq/antithesis-sdk-go)
BuildRequires:  go(github.com/appscodelabs/license-bill-of-materials)
BuildRequires:  go(github.com/ashanbrown/forbidigo/v2)
BuildRequires:  go(github.com/ashanbrown/makezero/v2)
BuildRequires:  go(github.com/beorn7/perks)
BuildRequires:  go(github.com/bgentry/speakeasy)
BuildRequires:  go(github.com/bitfield/gotestdox)
BuildRequires:  go(github.com/bkielbasa/cyclop)
BuildRequires:  go(github.com/blizzy78/varnamelen)
BuildRequires:  go(github.com/bmatcuk/doublestar/v4)
BuildRequires:  go(github.com/bombsimon/wsl/v4)
BuildRequires:  go(github.com/bombsimon/wsl/v5)
BuildRequires:  go(github.com/breml/bidichk)
BuildRequires:  go(github.com/breml/errchkjson)
BuildRequires:  go(github.com/butuzov/ireturn)
BuildRequires:  go(github.com/butuzov/mirror)
BuildRequires:  go(github.com/campoy/embedmd)
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
BuildRequires:  go(github.com/cheggaaa/pb/v3)
BuildRequires:  go(github.com/ckaznocha/intrange)
BuildRequires:  go(github.com/clipperhouse/displaywidth)
BuildRequires:  go(github.com/clipperhouse/uax29/v2)
BuildRequires:  go(github.com/cloudflare/cfssl)
BuildRequires:  go(github.com/coreos/go-semver)
BuildRequires:  go(github.com/coreos/go-systemd/v22)
BuildRequires:  go(github.com/creack/pty)
BuildRequires:  go(github.com/curioswitch/go-reassign)
BuildRequires:  go(github.com/daixiang0/gci)
BuildRequires:  go(github.com/dave/dst)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/denis-tingaikin/go-header)
BuildRequires:  go(github.com/dlclark/regexp2)
BuildRequires:  go(github.com/dnephin/pflag)
BuildRequires:  go(github.com/dustin/go-humanize)
BuildRequires:  go(github.com/ettle/strcase)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/fatih/structtag)
BuildRequires:  go(github.com/firefart/nonamedreturns)
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/fzipp/gocyclo)
BuildRequires:  go(github.com/ghostiam/protogetter)
BuildRequires:  go(github.com/go-critic/go-critic)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/go-sql-driver/mysql)
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
BuildRequires:  go(github.com/golang-jwt/jwt/v5)
BuildRequires:  go(github.com/golang/freetype)
BuildRequires:  go(github.com/golang/protobuf)
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
BuildRequires:  go(github.com/google/certificate-transparency-go)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-github/v60)
BuildRequires:  go(github.com/google/go-querystring)
BuildRequires:  go(github.com/google/shlex)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/google/yamlfmt)
BuildRequires:  go(github.com/gordonklaus/ineffassign)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/gostaticanalysis/analysisutil)
BuildRequires:  go(github.com/gostaticanalysis/comment)
BuildRequires:  go(github.com/gostaticanalysis/forcetypeassert)
BuildRequires:  go(github.com/gostaticanalysis/nilerr)
BuildRequires:  go(github.com/grpc-ecosystem/go-grpc-middleware/providers/prometheus)
BuildRequires:  go(github.com/grpc-ecosystem/go-grpc-middleware/v2)
BuildRequires:  go(github.com/grpc-ecosystem/grpc-gateway/v2)
BuildRequires:  go(github.com/hashicorp/go-immutable-radix/v2)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/hashicorp/golang-lru/v2)
BuildRequires:  go(github.com/hexops/gotextdiff)
BuildRequires:  go(github.com/inconshreveable/mousetrap)
BuildRequires:  go(github.com/jgautheron/goconst)
BuildRequires:  go(github.com/jjti/go-spancheck)
BuildRequires:  go(github.com/jmhodges/clock)
BuildRequires:  go(github.com/jmoiron/sqlx)
BuildRequires:  go(github.com/jonboulle/clockwork)
BuildRequires:  go(github.com/julz/importas)
BuildRequires:  go(github.com/karamaru-alpha/copyloopvar)
BuildRequires:  go(github.com/kisielk/errcheck)
BuildRequires:  go(github.com/kisielk/sqlstruct)
BuildRequires:  go(github.com/kkHAIKE/contextcheck)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/kr/text)
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
BuildRequires:  go(github.com/leonklingele/grouper)
BuildRequires:  go(github.com/lib/pq)
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)
BuildRequires:  go(github.com/macabu/inamedparam)
BuildRequires:  go(github.com/manuelarte/embeddedstructfieldcheck)
BuildRequires:  go(github.com/manuelarte/funcorder)
BuildRequires:  go(github.com/maratori/testableexamples)
BuildRequires:  go(github.com/maratori/testpackage)
BuildRequires:  go(github.com/matoous/godox)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/mattn/go-sqlite3)
BuildRequires:  go(github.com/mgechev/revive)
BuildRequires:  go(github.com/mitchellh/go-homedir)
BuildRequires:  go(github.com/mitchellh/mapstructure)
BuildRequires:  go(github.com/moricho/tparallel)
BuildRequires:  go(github.com/muesli/cancelreader)
BuildRequires:  go(github.com/munnerz/goautoneg)
BuildRequires:  go(github.com/nakabonne/nestif)
BuildRequires:  go(github.com/nishanths/exhaustive)
BuildRequires:  go(github.com/nishanths/predeclared)
BuildRequires:  go(github.com/nunnatsa/ginkgolinter)
BuildRequires:  go(github.com/olekukonko/cat)
BuildRequires:  go(github.com/olekukonko/errors)
BuildRequires:  go(github.com/olekukonko/ll)
BuildRequires:  go(github.com/olekukonko/tablewriter)
BuildRequires:  go(github.com/pelletier/go-toml)
BuildRequires:  go(github.com/pelletier/go-toml/v2)
BuildRequires:  go(github.com/phayes/checkstyle)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
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
BuildRequires:  go(github.com/sabhiram/go-gitignore)
BuildRequires:  go(github.com/sagikazarmark/locafero)
BuildRequires:  go(github.com/sanposhiho/wastedassign/v2)
BuildRequires:  go(github.com/santhosh-tekuri/jsonschema/v6)
BuildRequires:  go(github.com/sashamelentyev/interfacebloat)
BuildRequires:  go(github.com/sashamelentyev/usestdlibvars)
BuildRequires:  go(github.com/securego/gosec/v2)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/sivchari/containedctx)
BuildRequires:  go(github.com/soheilhy/cmux)
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
BuildRequires:  go(github.com/timakin/bodyclose)
BuildRequires:  go(github.com/timonwong/loggercheck)
BuildRequires:  go(github.com/tmc/grpc-websocket-proxy)
BuildRequires:  go(github.com/tomarrell/wrapcheck/v2)
BuildRequires:  go(github.com/tommy-muehle/go-mnd/v2)
BuildRequires:  go(github.com/ultraware/funlen)
BuildRequires:  go(github.com/ultraware/whitespace)
BuildRequires:  go(github.com/uudashr/gocognit)
BuildRequires:  go(github.com/uudashr/iface)
BuildRequires:  go(github.com/weppos/publicsuffix-go)
BuildRequires:  go(github.com/xen0n/gosmopolitan)
BuildRequires:  go(github.com/xiang90/probing)
BuildRequires:  go(github.com/xo/terminfo)
BuildRequires:  go(github.com/yagipy/maintidx)
BuildRequires:  go(github.com/yeya24/promlinter)
BuildRequires:  go(github.com/ykadowak/zerologlint)
BuildRequires:  go(github.com/zmap/zcrypto)
BuildRequires:  go(github.com/zmap/zlint/v3)
BuildRequires:  go(gitlab.com/bosi/decorder)
BuildRequires:  go(go-simpler.org/musttag)
BuildRequires:  go(go-simpler.org/sloglint)
BuildRequires:  go(go.augendre.info/arangolint)
BuildRequires:  go(go.augendre.info/fatcontext)
BuildRequires:  go(go.etcd.io/bbolt)
BuildRequires:  go(go.etcd.io/gofail)
BuildRequires:  go(go.etcd.io/protodoc)
BuildRequires:  go(go.etcd.io/raft/v3)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlptrace)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.opentelemetry.io/proto/otlp)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/exp/typeparams)
BuildRequires:  go(golang.org/x/image)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/telemetry)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(gonum.org/v1/gonum)
BuildRequires:  go(gonum.org/v1/plot)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/grpc/cmd/protoc-gen-go-grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/natefinch/lumberjack.v2)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(gotest.tools/gotestsum)
BuildRequires:  go(gotest.tools/v3)
BuildRequires:  go(honnef.co/go/tools)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/utils)
BuildRequires:  go(mvdan.cc/gofumpt)
BuildRequires:  go(mvdan.cc/unparam)
BuildRequires:  go(sigs.k8s.io/yaml)
BuildRequires:  go-rpm-macros

Provides:       go(go.etcd.io/etcd/api/v3) = %{version}
Provides:       go(go.etcd.io/etcd/api/v3/authpb) = %{version}
Provides:       go(go.etcd.io/etcd/api/v3/etcdserverpb) = %{version}
Provides:       go(go.etcd.io/etcd/api/v3/etcdserverpb/gw) = %{version}
Provides:       go(go.etcd.io/etcd/api/v3/membershippb) = %{version}
Provides:       go(go.etcd.io/etcd/api/v3/mvccpb) = %{version}
Provides:       go(go.etcd.io/etcd/api/v3/v3rpc/rpctypes) = %{version}
Provides:       go(go.etcd.io/etcd/api/v3/version) = %{version}
Provides:       go(go.etcd.io/etcd/api/v3/versionpb) = %{version}
Provides:       go(go.etcd.io/etcd/cache/v3) = %{version}
Provides:       go(go.etcd.io/etcd/client/pkg/v3) = %{version}
Provides:       go(go.etcd.io/etcd/client/pkg/v3/fileutil) = %{version}
Provides:       go(go.etcd.io/etcd/client/pkg/v3/logutil) = %{version}
Provides:       go(go.etcd.io/etcd/client/pkg/v3/pathutil) = %{version}
Provides:       go(go.etcd.io/etcd/client/pkg/v3/srv) = %{version}
Provides:       go(go.etcd.io/etcd/client/pkg/v3/systemd) = %{version}
Provides:       go(go.etcd.io/etcd/client/pkg/v3/testutil) = %{version}
Provides:       go(go.etcd.io/etcd/client/pkg/v3/tlsutil) = %{version}
Provides:       go(go.etcd.io/etcd/client/pkg/v3/transport) = %{version}
Provides:       go(go.etcd.io/etcd/client/pkg/v3/types) = %{version}
Provides:       go(go.etcd.io/etcd/client/pkg/v3/verify) = %{version}
Provides:       go(go.etcd.io/etcd/client/v3) = %{version}
Provides:       go(go.etcd.io/etcd/client/v3/clientv3util) = %{version}
Provides:       go(go.etcd.io/etcd/client/v3/concurrency) = %{version}
Provides:       go(go.etcd.io/etcd/client/v3/credentials) = %{version}
Provides:       go(go.etcd.io/etcd/client/v3/experimental/recipes) = %{version}
Provides:       go(go.etcd.io/etcd/client/v3/internal/endpoint) = %{version}
Provides:       go(go.etcd.io/etcd/client/v3/internal/resolver) = %{version}
Provides:       go(go.etcd.io/etcd/client/v3/kubernetes) = %{version}
Provides:       go(go.etcd.io/etcd/client/v3/leasing) = %{version}
Provides:       go(go.etcd.io/etcd/client/v3/mirror) = %{version}
Provides:       go(go.etcd.io/etcd/client/v3/mock/mockserver) = %{version}
Provides:       go(go.etcd.io/etcd/client/v3/namespace) = %{version}
Provides:       go(go.etcd.io/etcd/client/v3/naming) = %{version}
Provides:       go(go.etcd.io/etcd/client/v3/naming/endpoints) = %{version}
Provides:       go(go.etcd.io/etcd/client/v3/naming/endpoints/internal) = %{version}
Provides:       go(go.etcd.io/etcd/client/v3/naming/resolver) = %{version}
Provides:       go(go.etcd.io/etcd/client/v3/ordering) = %{version}
Provides:       go(go.etcd.io/etcd/client/v3/snapshot) = %{version}
Provides:       go(go.etcd.io/etcd/client/v3/yaml) = %{version}
Provides:       go(go.etcd.io/etcd/etcdctl/v3) = %{version}
Provides:       go(go.etcd.io/etcd/etcdctl/v3/ctlv3) = %{version}
Provides:       go(go.etcd.io/etcd/etcdctl/v3/ctlv3/command) = %{version}
Provides:       go(go.etcd.io/etcd/etcdctl/v3/util) = %{version}
Provides:       go(go.etcd.io/etcd/etcdutl/v3) = %{version}
Provides:       go(go.etcd.io/etcd/etcdutl/v3/etcdutl) = %{version}
Provides:       go(go.etcd.io/etcd/etcdutl/v3/snapshot) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/adt) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/cobrautl) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/contention) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/cpuutil) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/crc) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/debugutil) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/expect) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/featuregate) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/flags) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/grpctesting) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/httputil) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/idutil) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/ioutil) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/netutil) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/notify) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/osutil) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/pbutil) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/proxy) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/report) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/runtime) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/schedule) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/stringutil) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/traceutil) = %{version}
Provides:       go(go.etcd.io/etcd/pkg/v3/wait) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/auth) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/config) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/embed) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdmain) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/api) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/api/etcdhttp) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/api/etcdhttp/types) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/api/membership) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/api/rafthttp) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/api/snap) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/api/snap/snappb) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/api/v2error) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/api/v2stats) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/api/v2store) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/api/v3alarm) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/api/v3client) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/api/v3compactor) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/api/v3discovery) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/api/v3election) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/api/v3election/v3electionpb) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/api/v3election/v3electionpb/gw) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/api/v3lock) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/api/v3lock/v3lockpb) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/api/v3lock/v3lockpb/gw) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/api/v3rpc) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/apply) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/cindex) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/errors) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/read) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/txn) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/etcdserver/version) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/features) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/lease) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/lease/leasehttp) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/lease/leasepb) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/mock/mockstorage) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/mock/mockstore) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/mock/mockwait) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/proxy/grpcproxy) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/proxy/grpcproxy/adapter) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/proxy/grpcproxy/cache) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/proxy/tcpproxy) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/storage) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/storage/backend) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/storage/backend/testing) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/storage/datadir) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/storage/mvcc) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/storage/mvcc/testutil) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/storage/schema) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/storage/wal) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/storage/wal/testing) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/storage/wal/walpb) = %{version}
Provides:       go(go.etcd.io/etcd/server/v3/verify) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/antithesis/test-template/robustness/common) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/common) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/e2e) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/framework) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/framework/config) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/framework/e2e) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/framework/integration) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/framework/interfaces) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/framework/testutils) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/framework/unit) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/integration) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/integration/clientv3) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/integration/clientv3/connectivity) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/integration/clientv3/lease) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/robustness/client) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/robustness/failpoint) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/robustness/identity) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/robustness/model) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/robustness/options) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/robustness/random) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/robustness/report) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/robustness/scenarios) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/robustness/traffic) = %{version}
Provides:       go(go.etcd.io/etcd/tests/v3/robustness/validate) = %{version}
Provides:       go(go.etcd.io/etcd/tools/rw-heatmaps/v3) = %{version}
Provides:       go(go.etcd.io/etcd/tools/rw-heatmaps/v3/cmd) = %{version}
Provides:       go(go.etcd.io/etcd/tools/rw-heatmaps/v3/pkg/chart) = %{version}
Provides:       go(go.etcd.io/etcd/tools/rw-heatmaps/v3/pkg/dataset) = %{version}
Provides:       go(go.etcd.io/etcd/tools/testgrid-analysis/v3) = %{version}
Provides:       go(go.etcd.io/etcd/tools/testgrid-analysis/v3/cmd) = %{version}
Provides:       go(go.etcd.io/etcd/tools/v3) = %{version}
Provides:       go(go.etcd.io/etcd/v3) = %{version}
Provides:       go(go.etcd.io/etcd/v3/tools/benchmark/cmd) = %{version}
Provides:       go(go.etcd.io/etcd/v3/tools/proto-annotations/cmd) = %{version}

Requires:       go(github.com/GoogleCloudPlatform/testgrid)
Requires:       go(github.com/alexfalkowski/gocovmerge)
Requires:       go(github.com/anishathalye/porcupine)
Requires:       go(github.com/antithesishq/antithesis-sdk-go)
Requires:       go(github.com/appscodelabs/license-bill-of-materials)
Requires:       go(github.com/bgentry/speakeasy)
Requires:       go(github.com/cheggaaa/pb/v3)
Requires:       go(github.com/cloudflare/cfssl)
Requires:       go(github.com/coreos/go-semver)
Requires:       go(github.com/coreos/go-systemd/v22)
Requires:       go(github.com/creack/pty)
Requires:       go(github.com/dustin/go-humanize)
Requires:       go(github.com/golang-jwt/jwt/v5)
Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/golangci/golangci-lint/v2)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/go-github/v60)
Requires:       go(github.com/google/yamlfmt)
Requires:       go(github.com/grpc-ecosystem/go-grpc-middleware/providers/prometheus)
Requires:       go(github.com/grpc-ecosystem/go-grpc-middleware/v2)
Requires:       go(github.com/grpc-ecosystem/grpc-gateway/v2)
Requires:       go(github.com/jonboulle/clockwork)
Requires:       go(github.com/olekukonko/tablewriter)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/prometheus/client_model)
Requires:       go(github.com/prometheus/common)
Requires:       go(github.com/prometheus/procfs)
Requires:       go(github.com/ryancurrah/gomodguard)
Requires:       go(github.com/soheilhy/cmux)
Requires:       go(github.com/spf13/cobra)
Requires:       go(github.com/spf13/pflag)
Requires:       go(github.com/stretchr/testify)
Requires:       go(github.com/tmc/grpc-websocket-proxy)
Requires:       go(github.com/xiang90/probing)
Requires:       go(go.etcd.io/bbolt)
Requires:       go(go.etcd.io/gofail)
Requires:       go(go.etcd.io/protodoc)
Requires:       go(go.etcd.io/raft/v3)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc)
Requires:       go(go.opentelemetry.io/otel/sdk)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(go.uber.org/multierr)
Requires:       go(go.uber.org/zap)
Requires:       go(go.yaml.in/yaml/v2)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/time)
Requires:       go(golang.org/x/tools)
Requires:       go(gonum.org/v1/plot)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/genproto/googleapis/api)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/grpc/cmd/protoc-gen-go-grpc)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/natefinch/lumberjack.v2)
Requires:       go(gotest.tools/gotestsum)
Requires:       go(gotest.tools/v3)
Requires:       go(honnef.co/go/tools)
Requires:       go(k8s.io/utils)
Requires:       go(sigs.k8s.io/yaml)

%description
This package bundles the etcd API, clients, shared utilities, server, and
test modules from one repository snapshot. The removed version 2 client
remains in a separate compatibility package.

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
. go.etcd.io/etcd/v3 api cache etcdctl etcdutl pkg server tests client/pkg client/v3 tools/mod tools/rw-heatmaps tools/testgrid-analysis
api go.etcd.io/etcd/api/v3
cache go.etcd.io/etcd/cache/v3
etcdctl go.etcd.io/etcd/etcdctl/v3
etcdutl go.etcd.io/etcd/etcdutl/v3
pkg go.etcd.io/etcd/pkg/v3
server go.etcd.io/etcd/server/v3
tests go.etcd.io/etcd/tests/v3
client/pkg go.etcd.io/etcd/client/pkg/v3
client/v3 go.etcd.io/etcd/client/v3
tools/mod go.etcd.io/etcd/tools/v3
tools/rw-heatmaps go.etcd.io/etcd/tools/rw-heatmaps/v3
tools/testgrid-analysis go.etcd.io/etcd/tools/testgrid-analysis/v3
GO_MODULES

%check
%go_common
# Test the installed layout, including nested modules, without loading a
# second copy of the repository or using the system's older source package.
install -d "%{_builddir}/go/src"
cp -a "%{buildroot}%{go_sys_gopath}/." "%{_builddir}/go/src/"
_go_packages=$(go list -e -f '{{.ImportPath}}' go.etcd.io/etcd/...)
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
