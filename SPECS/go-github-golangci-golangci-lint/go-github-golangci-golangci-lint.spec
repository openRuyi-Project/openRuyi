# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           golangci-lint
%define go_import_path  github.com/golangci/golangci-lint/v2

Name:           go-github-golangci-golangci-lint
Version:        2.15.0
Release:        %autorelease
Summary:        Go linter aggregation and integration libraries
License:        BSD-3-Clause AND GPL-3.0-only AND MIT
URL:            https://github.com/golangci/golangci-lint
#!RemoteAsset:  sha256:5411598703f014f1128b209f3d46da6f9f2c99a68783c90f846b4db1c8c08742
Source0:        https://github.com/golangci/golangci-lint/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.26.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(4d63.com/gocheckcompilerdirectives)
BuildRequires:  go(4d63.com/gocheckcompilerdirectives/checkcompilerdirectives)
BuildRequires:  go(4d63.com/gochecknoglobals)
BuildRequires:  go(4d63.com/gochecknoglobals/checknoglobals)
BuildRequires:  go(charm.land/lipgloss/v2)
BuildRequires:  go(codeberg.org/chavacava/garif)
BuildRequires:  go(codeberg.org/polyfloyd/go-errorlint)
BuildRequires:  go(codeberg.org/polyfloyd/go-errorlint/errorlint)
BuildRequires:  go(dev.gaijin.team/go/exhaustruct/v4)
BuildRequires:  go(dev.gaijin.team/go/exhaustruct/v4/analyzer)
BuildRequires:  go(dev.gaijin.team/go/exhaustruct/v5)
BuildRequires:  go(dev.gaijin.team/go/exhaustruct/v5/analyzer)
BuildRequires:  go(dev.gaijin.team/go/golib)
BuildRequires:  go(github.com/4meepo/tagalign)
BuildRequires:  go(github.com/Abirdcfly/dupword)
BuildRequires:  go(github.com/AdminBenni/iota-mixing)
BuildRequires:  go(github.com/AdminBenni/iota-mixing/pkg/analyzer)
BuildRequires:  go(github.com/AdminBenni/iota-mixing/pkg/analyzer/flags)
BuildRequires:  go(github.com/AlwxSin/noinlineerr)
BuildRequires:  go(github.com/Antonboom/errname)
BuildRequires:  go(github.com/Antonboom/errname/pkg/analyzer)
BuildRequires:  go(github.com/Antonboom/nilnil)
BuildRequires:  go(github.com/Antonboom/nilnil/pkg/analyzer)
BuildRequires:  go(github.com/Antonboom/testifylint)
BuildRequires:  go(github.com/Antonboom/testifylint/analyzer)
BuildRequires:  go(github.com/BurntSushi/toml)
BuildRequires:  go(github.com/ClickHouse/ch-go)
BuildRequires:  go(github.com/ClickHouse/clickhouse-go-linter)
BuildRequires:  go(github.com/ClickHouse/clickhouse-go-linter/passes/chbatchclose)
BuildRequires:  go(github.com/ClickHouse/clickhouse-go-linter/passes/chrowserr)
BuildRequires:  go(github.com/ClickHouse/clickhouse-go/v2)
BuildRequires:  go(github.com/ClickHouse/clickhouse-go/v2/lib/driver)
BuildRequires:  go(github.com/Djarvur/go-err113)
BuildRequires:  go(github.com/Masterminds/semver/v3)
BuildRequires:  go(github.com/MirrexOne/unqueryvet)
BuildRequires:  go(github.com/MirrexOne/unqueryvet/pkg/config)
BuildRequires:  go(github.com/OpenPeeDeeP/depguard/v2)
BuildRequires:  go(github.com/alecthomas/chroma/v2)
BuildRequires:  go(github.com/alecthomas/chroma/v2/quick)
BuildRequires:  go(github.com/alecthomas/go-check-sumtype)
BuildRequires:  go(github.com/alexkohler/nakedret/v2)
BuildRequires:  go(github.com/alexkohler/prealloc)
BuildRequires:  go(github.com/alexkohler/prealloc/pkg)
BuildRequires:  go(github.com/alfatraining/structtag)
BuildRequires:  go(github.com/alingse/asasalint)
BuildRequires:  go(github.com/alingse/nilnesserr)
BuildRequires:  go(github.com/arangodb/go-driver/v2)
BuildRequires:  go(github.com/arangodb/go-driver/v2/arangodb)
BuildRequires:  go(github.com/arangodb/go-velocypack)
BuildRequires:  go(github.com/ashanbrown/forbidigo/v2)
BuildRequires:  go(github.com/ashanbrown/forbidigo/v2/forbidigo)
BuildRequires:  go(github.com/ashanbrown/makezero/v2)
BuildRequires:  go(github.com/ashanbrown/makezero/v2/makezero)
BuildRequires:  go(github.com/beorn7/perks)
BuildRequires:  go(github.com/bkielbasa/cyclop)
BuildRequires:  go(github.com/bkielbasa/cyclop/pkg/analyzer)
BuildRequires:  go(github.com/blizzy78/varnamelen)
BuildRequires:  go(github.com/bombsimon/wsl/v4)
BuildRequires:  go(github.com/bombsimon/wsl/v5)
BuildRequires:  go(github.com/breml/bidichk)
BuildRequires:  go(github.com/breml/bidichk/pkg/bidichk)
BuildRequires:  go(github.com/breml/errchkjson)
BuildRequires:  go(github.com/butuzov/ireturn)
BuildRequires:  go(github.com/butuzov/ireturn/analyzer)
BuildRequires:  go(github.com/butuzov/mirror)
BuildRequires:  go(github.com/catenacyber/perfsprint)
BuildRequires:  go(github.com/catenacyber/perfsprint/analyzer)
BuildRequires:  go(github.com/ccojocar/zxcvbn-go)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/charithe/durationcheck)
BuildRequires:  go(github.com/charmbracelet/colorprofile)
BuildRequires:  go(github.com/charmbracelet/ultraviolet)
BuildRequires:  go(github.com/charmbracelet/x/ansi)
BuildRequires:  go(github.com/charmbracelet/x/term)
BuildRequires:  go(github.com/charmbracelet/x/termios)
BuildRequires:  go(github.com/charmbracelet/x/windows)
BuildRequires:  go(github.com/ckaznocha/intrange)
BuildRequires:  go(github.com/clipperhouse/displaywidth)
BuildRequires:  go(github.com/clipperhouse/uax29/v2)
BuildRequires:  go(github.com/curioswitch/go-reassign)
BuildRequires:  go(github.com/daixiang0/gci)
BuildRequires:  go(github.com/daixiang0/gci/pkg/config)
BuildRequires:  go(github.com/daixiang0/gci/pkg/gci)
BuildRequires:  go(github.com/daixiang0/gci/pkg/log)
BuildRequires:  go(github.com/daixiang0/gci/pkg/parse)
BuildRequires:  go(github.com/daixiang0/gci/pkg/section)
BuildRequires:  go(github.com/daixiang0/gci/pkg/specificity)
BuildRequires:  go(github.com/dave/dst)
BuildRequires:  go(github.com/dchest/siphash)
BuildRequires:  go(github.com/denis-tingaikin/go-header)
BuildRequires:  go(github.com/dlclark/regexp2)
BuildRequires:  go(github.com/dlclark/regexp2/v2)
BuildRequires:  go(github.com/ebitengine/purego)
BuildRequires:  go(github.com/ettle/strcase)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/fatih/structtag)
BuildRequires:  go(github.com/firefart/nonamedreturns)
BuildRequires:  go(github.com/firefart/nonamedreturns/analyzer)
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/fzipp/gocyclo)
BuildRequires:  go(github.com/ghostiam/protogetter)
BuildRequires:  go(github.com/go-critic/go-critic)
BuildRequires:  go(github.com/go-critic/go-critic/checkers)
BuildRequires:  go(github.com/go-critic/go-critic/linter)
BuildRequires:  go(github.com/go-faster/city)
BuildRequires:  go(github.com/go-faster/errors)
BuildRequires:  go(github.com/go-kit/log)
BuildRequires:  go(github.com/go-logfmt/logfmt)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/go-ole/go-ole)
BuildRequires:  go(github.com/go-task/slim-sprig/v3)
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
BuildRequires:  go(github.com/godoc-lint/godoc-lint/pkg/compose)
BuildRequires:  go(github.com/godoc-lint/godoc-lint/pkg/config)
BuildRequires:  go(github.com/godoc-lint/godoc-lint/pkg/model)
BuildRequires:  go(github.com/gofrs/flock)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/golangci/asciicheck)
BuildRequires:  go(github.com/golangci/canonicalheader)
BuildRequires:  go(github.com/golangci/dupl)
BuildRequires:  go(github.com/golangci/dupl/lib)
BuildRequires:  go(github.com/golangci/go-printf-func-name)
BuildRequires:  go(github.com/golangci/go-printf-func-name/pkg/analyzer)
BuildRequires:  go(github.com/golangci/gofmt)
BuildRequires:  go(github.com/golangci/golines)
BuildRequires:  go(github.com/golangci/golines/shorten)
BuildRequires:  go(github.com/golangci/misspell)
BuildRequires:  go(github.com/golangci/plugin-module-register)
BuildRequires:  go(github.com/golangci/plugin-module-register/register)
BuildRequires:  go(github.com/golangci/revgrep)
BuildRequires:  go(github.com/golangci/rowserrcheck)
BuildRequires:  go(github.com/golangci/rowserrcheck/passes/rowserr)
BuildRequires:  go(github.com/golangci/swaggoswag)
BuildRequires:  go(github.com/golangci/unconvert)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/pprof)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/gordonklaus/ineffassign)
BuildRequires:  go(github.com/gordonklaus/ineffassign/pkg/ineffassign)
BuildRequires:  go(github.com/gostaticanalysis/analysisutil)
BuildRequires:  go(github.com/gostaticanalysis/comment)
BuildRequires:  go(github.com/gostaticanalysis/forcetypeassert)
BuildRequires:  go(github.com/gostaticanalysis/nilerr)
BuildRequires:  go(github.com/hashicorp/go-immutable-radix/v2)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/hashicorp/golang-lru/v2)
BuildRequires:  go(github.com/hashicorp/hcl)
BuildRequires:  go(github.com/hexops/gotextdiff)
BuildRequires:  go(github.com/imfing/hextra)
BuildRequires:  go(github.com/inconshreveable/mousetrap)
BuildRequires:  go(github.com/jgautheron/goconst)
BuildRequires:  go(github.com/jjti/go-spancheck)
BuildRequires:  go(github.com/julz/importas)
BuildRequires:  go(github.com/karamaru-alpha/copyloopvar)
BuildRequires:  go(github.com/kisielk/errcheck)
BuildRequires:  go(github.com/kisielk/errcheck/errcheck)
BuildRequires:  go(github.com/kkHAIKE/contextcheck)
BuildRequires:  go(github.com/kkdai/maglev)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/kulti/thelper)
BuildRequires:  go(github.com/kulti/thelper/pkg/analyzer)
BuildRequires:  go(github.com/kunwardeep/paralleltest)
BuildRequires:  go(github.com/kunwardeep/paralleltest/pkg/paralleltest)
BuildRequires:  go(github.com/ldez/exptostd)
BuildRequires:  go(github.com/ldez/gomoddirectives)
BuildRequires:  go(github.com/ldez/grignotin)
BuildRequires:  go(github.com/ldez/grignotin/goenv)
BuildRequires:  go(github.com/ldez/grignotin/gomod)
BuildRequires:  go(github.com/ldez/structtags)
BuildRequires:  go(github.com/ldez/tagliatelle)
BuildRequires:  go(github.com/ldez/usetesting)
BuildRequires:  go(github.com/leonklingele/grouper)
BuildRequires:  go(github.com/leonklingele/grouper/pkg/analyzer)
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)
BuildRequires:  go(github.com/lufia/plan9stats)
BuildRequires:  go(github.com/macabu/inamedparam)
BuildRequires:  go(github.com/magiconair/properties)
BuildRequires:  go(github.com/manuelarte/embeddedstructfieldcheck)
BuildRequires:  go(github.com/manuelarte/embeddedstructfieldcheck/analyzer)
BuildRequires:  go(github.com/manuelarte/funcorder)
BuildRequires:  go(github.com/manuelarte/funcorder/analyzer)
BuildRequires:  go(github.com/maratori/testableexamples)
BuildRequires:  go(github.com/maratori/testableexamples/pkg/testableexamples)
BuildRequires:  go(github.com/maratori/testpackage)
BuildRequires:  go(github.com/maratori/testpackage/pkg/testpackage)
BuildRequires:  go(github.com/matoous/godox)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/matttproud/golang_protobuf_extensions)
BuildRequires:  go(github.com/mgechev/revive)
BuildRequires:  go(github.com/mgechev/revive/config)
BuildRequires:  go(github.com/mgechev/revive/lint)
BuildRequires:  go(github.com/mgechev/revive/rule)
BuildRequires:  go(github.com/mitchellh/go-homedir)
BuildRequires:  go(github.com/mitchellh/mapstructure)
BuildRequires:  go(github.com/moricho/tparallel)
BuildRequires:  go(github.com/muesli/cancelreader)
BuildRequires:  go(github.com/nakabonne/nestif)
BuildRequires:  go(github.com/nishanths/exhaustive)
BuildRequires:  go(github.com/nishanths/exhaustive/passes/enumerated)
BuildRequires:  go(github.com/nishanths/exhaustive/passes/exhaustive)
BuildRequires:  go(github.com/nishanths/predeclared)
BuildRequires:  go(github.com/nishanths/predeclared/passes/predeclared)
BuildRequires:  go(github.com/nunnatsa/ginkgolinter)
BuildRequires:  go(github.com/nunnatsa/ginkgolinter/config)
BuildRequires:  go(github.com/onsi/ginkgo/v2)
BuildRequires:  go(github.com/onsi/gomega)
BuildRequires:  go(github.com/paulmach/orb)
BuildRequires:  go(github.com/pelletier/go-toml)
BuildRequires:  go(github.com/pelletier/go-toml/v2)
BuildRequires:  go(github.com/pierrec/lz4/v4)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/power-devops/perfstat)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_golang/prometheus)
BuildRequires:  go(github.com/prometheus/client_golang/prometheus/promauto)
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
BuildRequires:  go(github.com/rogpeppe/go-internal/diff)
BuildRequires:  go(github.com/rogpeppe/go-internal/lockedfile)
BuildRequires:  go(github.com/rogpeppe/go-internal/robustio)
BuildRequires:  go(github.com/rs/zerolog)
BuildRequires:  go(github.com/rs/zerolog/log)
BuildRequires:  go(github.com/ryancurrah/gomodguard)
BuildRequires:  go(github.com/ryancurrah/gomodguard/v2)
BuildRequires:  go(github.com/ryanrolds/sqlclosecheck)
BuildRequires:  go(github.com/ryanrolds/sqlclosecheck/pkg/analyzer)
BuildRequires:  go(github.com/sanposhiho/wastedassign/v2)
BuildRequires:  go(github.com/santhosh-tekuri/jsonschema/v6)
BuildRequires:  go(github.com/sashamelentyev/interfacebloat)
BuildRequires:  go(github.com/sashamelentyev/interfacebloat/pkg/analyzer)
BuildRequires:  go(github.com/sashamelentyev/usestdlibvars)
BuildRequires:  go(github.com/sashamelentyev/usestdlibvars/pkg/analyzer)
BuildRequires:  go(github.com/securego/gosec/v2)
BuildRequires:  go(github.com/securego/gosec/v2/analyzers)
BuildRequires:  go(github.com/securego/gosec/v2/issue)
BuildRequires:  go(github.com/securego/gosec/v2/rules)
BuildRequires:  go(github.com/segmentio/asm)
BuildRequires:  go(github.com/shirou/gopsutil/v4)
BuildRequires:  go(github.com/shirou/gopsutil/v4/process)
BuildRequires:  go(github.com/shopspring/decimal)
BuildRequires:  go(github.com/shurcooL/githubv4)
BuildRequires:  go(github.com/shurcooL/graphql)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/sivchari/containedctx)
BuildRequires:  go(github.com/sonatard/noctx)
BuildRequires:  go(github.com/sourcegraph/go-diff)
BuildRequires:  go(github.com/sourcegraph/go-diff/diff)
BuildRequires:  go(github.com/spf13/afero)
BuildRequires:  go(github.com/spf13/cast)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/jwalterweatherman)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/spf13/viper)
BuildRequires:  go(github.com/ssgreg/nlreturn/v2)
BuildRequires:  go(github.com/ssgreg/nlreturn/v2/pkg/nlreturn)
BuildRequires:  go(github.com/stbenjam/no-sprintf-host-port)
BuildRequires:  go(github.com/stbenjam/no-sprintf-host-port/pkg/analyzer)
BuildRequires:  go(github.com/stretchr/objx)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/assert)
BuildRequires:  go(github.com/stretchr/testify/mock)
BuildRequires:  go(github.com/stretchr/testify/require)
BuildRequires:  go(github.com/stretchr/testify/suite)
BuildRequires:  go(github.com/subosito/gotenv)
BuildRequires:  go(github.com/tetafro/godot)
BuildRequires:  go(github.com/timakin/bodyclose)
BuildRequires:  go(github.com/timakin/bodyclose/passes/bodyclose)
BuildRequires:  go(github.com/timonwong/loggercheck)
BuildRequires:  go(github.com/tklauser/go-sysconf)
BuildRequires:  go(github.com/tklauser/numcpus)
BuildRequires:  go(github.com/tomarrell/wrapcheck/v2)
BuildRequires:  go(github.com/tomarrell/wrapcheck/v2/wrapcheck)
BuildRequires:  go(github.com/tommy-muehle/go-mnd/v2)
BuildRequires:  go(github.com/ultraware/funlen)
BuildRequires:  go(github.com/ultraware/whitespace)
BuildRequires:  go(github.com/uudashr/gocognit)
BuildRequires:  go(github.com/uudashr/iface)
BuildRequires:  go(github.com/uudashr/iface/identical)
BuildRequires:  go(github.com/uudashr/iface/opaque)
BuildRequires:  go(github.com/uudashr/iface/unexported)
BuildRequires:  go(github.com/uudashr/iface/unused)
BuildRequires:  go(github.com/uudashr/iface/unusedmethod)
BuildRequires:  go(github.com/valyala/bytebufferpool)
BuildRequires:  go(github.com/valyala/quicktemplate)
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
BuildRequires:  go(go.augendre.info/arangolint/pkg/analyzer)
BuildRequires:  go(go.augendre.info/fatcontext)
BuildRequires:  go(go.augendre.info/fatcontext/pkg/analyzer)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/codes)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/exp/maps)
BuildRequires:  go(golang.org/x/exp/slices)
BuildRequires:  go(golang.org/x/exp/typeparams)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/mod/modfile)
BuildRequires:  go(golang.org/x/mod/sumdb/dirhash)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sync/errgroup)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/sys/windows)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/appends)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/asmdecl)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/assign)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/atomic)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/atomicalign)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/bools)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/buildssa)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/buildtag)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/cgocall)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/composite)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/copylock)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/ctrlflow)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/deepequalerrors)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/defers)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/directive)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/errorsas)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/fieldalignment)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/findcall)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/framepointer)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/hostport)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/httpmux)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/httpresponse)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/ifaceassert)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/inline)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/inspect)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/loopclosure)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/lostcancel)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/modernize)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/nilfunc)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/nilness)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/pkgfact)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/printf)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/reflectvaluecompare)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/shadow)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/shift)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/sigchanyzer)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/slog)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/sortslice)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/stdmethods)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/stdversion)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/stringintconv)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/structtag)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/testinggoroutine)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/tests)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/timeformat)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/unmarshal)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/unreachable)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/unsafeptr)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/unusedresult)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/unusedwrite)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/waitgroup)
BuildRequires:  go(golang.org/x/tools/go/ast/inspector)
BuildRequires:  go(golang.org/x/tools/go/gcexportdata)
BuildRequires:  go(golang.org/x/tools/go/packages)
BuildRequires:  go(golang.org/x/tools/go/packages/packagestest)
BuildRequires:  go(golang.org/x/tools/go/types/objectpath)
BuildRequires:  go(golang.org/x/tools/imports)
BuildRequires:  go(golang.org/x/xerrors)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/grpc/codes)
BuildRequires:  go(google.golang.org/grpc/status)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(google.golang.org/protobuf/reflect/protoreflect)
BuildRequires:  go(google.golang.org/protobuf/runtime/protoimpl)
BuildRequires:  go(gopkg.in/ini.v1)
BuildRequires:  go(gopkg.in/yaml.v2)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(honnef.co/go/tools)
BuildRequires:  go(honnef.co/go/tools/analysis/facts/directives)
BuildRequires:  go(honnef.co/go/tools/analysis/facts/generated)
BuildRequires:  go(honnef.co/go/tools/analysis/lint)
BuildRequires:  go(honnef.co/go/tools/config)
BuildRequires:  go(honnef.co/go/tools/quickfix)
BuildRequires:  go(honnef.co/go/tools/simple)
BuildRequires:  go(honnef.co/go/tools/staticcheck)
BuildRequires:  go(honnef.co/go/tools/stylecheck)
BuildRequires:  go(honnef.co/go/tools/unused)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(mvdan.cc/gofumpt)
BuildRequires:  go(mvdan.cc/gofumpt/format)
BuildRequires:  go(mvdan.cc/unparam)
BuildRequires:  go(mvdan.cc/unparam/check)

# External commands used by the upstream tests.
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  make

# Export the source module roots and every installed Go package.
Provides:       go(github.com/golangci/docs) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/cmd/golangci-lint) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/internal/cache) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/internal/errorutil) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/internal/go/base) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/internal/go/cache) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/internal/go/cacheprog) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/internal/go/mmap) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/internal/go/quoted) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/internal/go/testenv) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/internal/x/tools/diff) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/internal/x/tools/diff/lcs) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/internal/x/tools/driverutil) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/jsonschema) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/commands) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/commands/internal) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/commands/internal/migrate) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/commands/internal/migrate/cloner) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/commands/internal/migrate/fakeloader) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/commands/internal/migrate/parser) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/commands/internal/migrate/ptr) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/commands/internal/migrate/versionone) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/commands/internal/migrate/versiontwo) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/config) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/exitcodes) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/fsutils) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/goanalysis) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/goanalysis/load) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/goanalysis/pkgerrors) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/goformat) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/goformatters) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/goformatters/gci) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/goformatters/gci/internal/config) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/goformatters/gci/internal/section) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/goformatters/gofmt) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/goformatters/gofumpt) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/goformatters/goimports) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/goformatters/golines) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/goformatters/internal) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/goformatters/swaggo) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/arangolint) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/asasalint) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/asciicheck) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/bidichk) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/bodyclose) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/canonicalheader) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/clickhouselint) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/containedctx) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/contextcheck) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/copyloopvar) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/cyclop) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/decorder) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/depguard) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/dogsled) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/dupl) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/dupword) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/durationcheck) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/embeddedstructfieldcheck) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/err113) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/errcheck) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/errchkjson) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/errname) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/errorlint) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/exhaustive) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/exhaustruct) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/exptostd) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/fatcontext) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/forbidigo) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/forcetypeassert) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/funcorder) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/funlen) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/gci) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/ginkgolinter) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/gocheckcompilerdirectives) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/gochecknoglobals) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/gochecknoinits) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/gochecksumtype) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/gocognit) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/goconst) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/gocritic) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/gocyclo) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/godoclint) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/godot) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/godox) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/gofmt) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/gofumpt) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/goheader) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/goimports) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/golines) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/gomoddirectives) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/gomodguard) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/goprintffuncname) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/gosec) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/gosmopolitan) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/govet) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/grouper) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/iface) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/importas) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/inamedparam) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/ineffassign) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/interfacebloat) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/internal) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/intrange) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/iotamixing) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/ireturn) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/lll) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/loggercheck) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/maintidx) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/makezero) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/mirror) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/misspell) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/mnd) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/modernize) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/musttag) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/nakedret) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/nestif) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/nilerr) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/nilnesserr) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/nilnil) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/nlreturn) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/noctx) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/noinlineerr) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/nolintlint) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/nolintlint/internal) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/nonamedreturns) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/nosprintfhostport) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/paralleltest) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/perfsprint) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/prealloc) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/predeclared) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/promlinter) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/protogetter) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/reassign) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/recvcheck) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/revive) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/rowserrcheck) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/sloglint) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/spancheck) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/sqlclosecheck) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/staticcheck) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/swaggo) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/tagalign) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/tagliatelle) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/testableexamples) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/testifylint) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/testpackage) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/thelper) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/tparallel) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/unconvert) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/unparam) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/unqueryvet) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/unused) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/usestdlibvars) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/usetesting) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/varnamelen) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/wastedassign) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/whitespace) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/wrapcheck) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/wsl) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/golinters/zerologlint) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/goutil) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/lint) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/lint/linter) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/lint/lintersdb) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/logutils) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/printers) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/report) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/result) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/result/processors) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/pkg/timeutils) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/scripts/gen_github_action_config) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/scripts/print_ast) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/scripts/website/copy_jsonschema) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/scripts/website/dump_info) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/scripts/website/expand_templates) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/scripts/website/github) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/scripts/website/types) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/test/testdata_etc/abspath) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/test/testdata_etc/unused_exported) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/test/testdata_etc/unused_exported/lib) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/test/testshared) = %{version}
Provides:       go(github.com/golangci/golangci-lint/v2/test/testshared/integration) = %{version}

Requires:       go(4d63.com/gocheckcompilerdirectives/checkcompilerdirectives)
Requires:       go(4d63.com/gochecknoglobals/checknoglobals)
Requires:       go(charm.land/lipgloss/v2)
Requires:       go(codeberg.org/polyfloyd/go-errorlint/errorlint)
Requires:       go(dev.gaijin.team/go/exhaustruct/v4/analyzer)
Requires:       go(dev.gaijin.team/go/exhaustruct/v5/analyzer)
Requires:       go(github.com/4meepo/tagalign)
Requires:       go(github.com/Abirdcfly/dupword)
Requires:       go(github.com/AdminBenni/iota-mixing/pkg/analyzer)
Requires:       go(github.com/AdminBenni/iota-mixing/pkg/analyzer/flags)
Requires:       go(github.com/AlwxSin/noinlineerr)
Requires:       go(github.com/Antonboom/errname/pkg/analyzer)
Requires:       go(github.com/Antonboom/nilnil/pkg/analyzer)
Requires:       go(github.com/Antonboom/testifylint/analyzer)
Requires:       go(github.com/BurntSushi/toml)
Requires:       go(github.com/ClickHouse/clickhouse-go-linter/passes/chbatchclose)
Requires:       go(github.com/ClickHouse/clickhouse-go-linter/passes/chrowserr)
Requires:       go(github.com/Djarvur/go-err113)
Requires:       go(github.com/Masterminds/semver/v3)
Requires:       go(github.com/MirrexOne/unqueryvet)
Requires:       go(github.com/MirrexOne/unqueryvet/pkg/config)
Requires:       go(github.com/OpenPeeDeeP/depguard/v2)
Requires:       go(github.com/alecthomas/chroma/v2/quick)
Requires:       go(github.com/alecthomas/go-check-sumtype)
Requires:       go(github.com/alexkohler/nakedret/v2)
Requires:       go(github.com/alexkohler/prealloc/pkg)
Requires:       go(github.com/alingse/asasalint)
Requires:       go(github.com/alingse/nilnesserr)
Requires:       go(github.com/ashanbrown/forbidigo/v2/forbidigo)
Requires:       go(github.com/ashanbrown/makezero/v2/makezero)
Requires:       go(github.com/bkielbasa/cyclop/pkg/analyzer)
Requires:       go(github.com/blizzy78/varnamelen)
Requires:       go(github.com/bombsimon/wsl/v4)
Requires:       go(github.com/bombsimon/wsl/v5)
Requires:       go(github.com/breml/bidichk/pkg/bidichk)
Requires:       go(github.com/breml/errchkjson)
Requires:       go(github.com/butuzov/ireturn/analyzer)
Requires:       go(github.com/butuzov/mirror)
Requires:       go(github.com/catenacyber/perfsprint/analyzer)
Requires:       go(github.com/charithe/durationcheck)
Requires:       go(github.com/ckaznocha/intrange)
Requires:       go(github.com/curioswitch/go-reassign)
Requires:       go(github.com/daixiang0/gci/pkg/config)
Requires:       go(github.com/daixiang0/gci/pkg/gci)
Requires:       go(github.com/daixiang0/gci/pkg/log)
Requires:       go(github.com/daixiang0/gci/pkg/parse)
Requires:       go(github.com/daixiang0/gci/pkg/section)
Requires:       go(github.com/daixiang0/gci/pkg/specificity)
Requires:       go(github.com/denis-tingaikin/go-header)
Requires:       go(github.com/fatih/color)
Requires:       go(github.com/firefart/nonamedreturns/analyzer)
Requires:       go(github.com/fzipp/gocyclo)
Requires:       go(github.com/ghostiam/protogetter)
Requires:       go(github.com/go-critic/go-critic/checkers)
Requires:       go(github.com/go-critic/go-critic/linter)
Requires:       go(github.com/go-viper/mapstructure/v2)
Requires:       go(github.com/go-xmlfmt/xmlfmt)
Requires:       go(github.com/godoc-lint/godoc-lint/pkg/compose)
Requires:       go(github.com/godoc-lint/godoc-lint/pkg/config)
Requires:       go(github.com/godoc-lint/godoc-lint/pkg/model)
Requires:       go(github.com/gofrs/flock)
Requires:       go(github.com/golangci/asciicheck)
Requires:       go(github.com/golangci/canonicalheader)
Requires:       go(github.com/golangci/dupl/lib)
Requires:       go(github.com/golangci/go-printf-func-name/pkg/analyzer)
Requires:       go(github.com/golangci/gofmt)
Requires:       go(github.com/golangci/golines/shorten)
Requires:       go(github.com/golangci/misspell)
Requires:       go(github.com/golangci/plugin-module-register/register)
Requires:       go(github.com/golangci/revgrep)
Requires:       go(github.com/golangci/rowserrcheck/passes/rowserr)
Requires:       go(github.com/golangci/swaggoswag)
Requires:       go(github.com/golangci/unconvert)
Requires:       go(github.com/gordonklaus/ineffassign/pkg/ineffassign)
Requires:       go(github.com/gostaticanalysis/forcetypeassert)
Requires:       go(github.com/gostaticanalysis/nilerr)
Requires:       go(github.com/hashicorp/go-version)
Requires:       go(github.com/jgautheron/goconst)
Requires:       go(github.com/jjti/go-spancheck)
Requires:       go(github.com/julz/importas)
Requires:       go(github.com/karamaru-alpha/copyloopvar)
Requires:       go(github.com/kisielk/errcheck/errcheck)
Requires:       go(github.com/kkHAIKE/contextcheck)
Requires:       go(github.com/kulti/thelper/pkg/analyzer)
Requires:       go(github.com/kunwardeep/paralleltest/pkg/paralleltest)
Requires:       go(github.com/ldez/exptostd)
Requires:       go(github.com/ldez/gomoddirectives)
Requires:       go(github.com/ldez/grignotin/goenv)
Requires:       go(github.com/ldez/grignotin/gomod)
Requires:       go(github.com/ldez/tagliatelle)
Requires:       go(github.com/ldez/usetesting)
Requires:       go(github.com/leonklingele/grouper/pkg/analyzer)
Requires:       go(github.com/macabu/inamedparam)
Requires:       go(github.com/manuelarte/embeddedstructfieldcheck/analyzer)
Requires:       go(github.com/manuelarte/funcorder/analyzer)
Requires:       go(github.com/maratori/testableexamples/pkg/testableexamples)
Requires:       go(github.com/maratori/testpackage/pkg/testpackage)
Requires:       go(github.com/matoous/godox)
Requires:       go(github.com/mattn/go-colorable)
Requires:       go(github.com/mgechev/revive/config)
Requires:       go(github.com/mgechev/revive/lint)
Requires:       go(github.com/mgechev/revive/rule)
Requires:       go(github.com/mitchellh/go-homedir)
Requires:       go(github.com/moricho/tparallel)
Requires:       go(github.com/nakabonne/nestif)
Requires:       go(github.com/nishanths/exhaustive/passes/enumerated)
Requires:       go(github.com/nishanths/exhaustive/passes/exhaustive)
Requires:       go(github.com/nishanths/predeclared/passes/predeclared)
Requires:       go(github.com/nunnatsa/ginkgolinter)
Requires:       go(github.com/nunnatsa/ginkgolinter/config)
Requires:       go(github.com/pelletier/go-toml/v2)
Requires:       go(github.com/quasilyte/go-ruleguard/dsl)
Requires:       go(github.com/raeperd/recvcheck)
Requires:       go(github.com/rogpeppe/go-internal/diff)
Requires:       go(github.com/rogpeppe/go-internal/lockedfile)
Requires:       go(github.com/rogpeppe/go-internal/robustio)
Requires:       go(github.com/ryancurrah/gomodguard)
Requires:       go(github.com/ryancurrah/gomodguard/v2)
Requires:       go(github.com/ryanrolds/sqlclosecheck/pkg/analyzer)
Requires:       go(github.com/sanposhiho/wastedassign/v2)
Requires:       go(github.com/santhosh-tekuri/jsonschema/v6)
Requires:       go(github.com/sashamelentyev/interfacebloat/pkg/analyzer)
Requires:       go(github.com/sashamelentyev/usestdlibvars/pkg/analyzer)
Requires:       go(github.com/securego/gosec/v2)
Requires:       go(github.com/securego/gosec/v2/analyzers)
Requires:       go(github.com/securego/gosec/v2/issue)
Requires:       go(github.com/securego/gosec/v2/rules)
Requires:       go(github.com/shurcooL/githubv4)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(github.com/sivchari/containedctx)
Requires:       go(github.com/sonatard/noctx)
Requires:       go(github.com/sourcegraph/go-diff/diff)
Requires:       go(github.com/spf13/cobra)
Requires:       go(github.com/spf13/pflag)
Requires:       go(github.com/spf13/viper)
Requires:       go(github.com/ssgreg/nlreturn/v2/pkg/nlreturn)
Requires:       go(github.com/stbenjam/no-sprintf-host-port/pkg/analyzer)
Requires:       go(github.com/stretchr/testify/assert)
Requires:       go(github.com/stretchr/testify/mock)
Requires:       go(github.com/stretchr/testify/require)
Requires:       go(github.com/tetafro/godot)
Requires:       go(github.com/timakin/bodyclose/passes/bodyclose)
Requires:       go(github.com/timonwong/loggercheck)
Requires:       go(github.com/tomarrell/wrapcheck/v2/wrapcheck)
Requires:       go(github.com/tommy-muehle/go-mnd/v2)
Requires:       go(github.com/ultraware/funlen)
Requires:       go(github.com/ultraware/whitespace)
Requires:       go(github.com/uudashr/gocognit)
Requires:       go(github.com/uudashr/iface/identical)
Requires:       go(github.com/uudashr/iface/opaque)
Requires:       go(github.com/uudashr/iface/unexported)
Requires:       go(github.com/uudashr/iface/unused)
Requires:       go(github.com/uudashr/iface/unusedmethod)
Requires:       go(github.com/xen0n/gosmopolitan)
Requires:       go(github.com/yagipy/maintidx)
Requires:       go(github.com/yeya24/promlinter)
Requires:       go(github.com/ykadowak/zerologlint)
Requires:       go(gitlab.com/bosi/decorder)
Requires:       go(go-simpler.org/musttag)
Requires:       go(go-simpler.org/sloglint)
Requires:       go(go.augendre.info/arangolint/pkg/analyzer)
Requires:       go(go.augendre.info/fatcontext/pkg/analyzer)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(golang.org/x/mod/modfile)
Requires:       go(golang.org/x/mod/sumdb/dirhash)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/sync/errgroup)
Requires:       go(golang.org/x/sys/windows)
Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/passes/appends)
Requires:       go(golang.org/x/tools/go/analysis/passes/asmdecl)
Requires:       go(golang.org/x/tools/go/analysis/passes/assign)
Requires:       go(golang.org/x/tools/go/analysis/passes/atomic)
Requires:       go(golang.org/x/tools/go/analysis/passes/atomicalign)
Requires:       go(golang.org/x/tools/go/analysis/passes/bools)
Requires:       go(golang.org/x/tools/go/analysis/passes/buildssa)
Requires:       go(golang.org/x/tools/go/analysis/passes/buildtag)
Requires:       go(golang.org/x/tools/go/analysis/passes/cgocall)
Requires:       go(golang.org/x/tools/go/analysis/passes/composite)
Requires:       go(golang.org/x/tools/go/analysis/passes/copylock)
Requires:       go(golang.org/x/tools/go/analysis/passes/ctrlflow)
Requires:       go(golang.org/x/tools/go/analysis/passes/deepequalerrors)
Requires:       go(golang.org/x/tools/go/analysis/passes/defers)
Requires:       go(golang.org/x/tools/go/analysis/passes/directive)
Requires:       go(golang.org/x/tools/go/analysis/passes/errorsas)
Requires:       go(golang.org/x/tools/go/analysis/passes/fieldalignment)
Requires:       go(golang.org/x/tools/go/analysis/passes/findcall)
Requires:       go(golang.org/x/tools/go/analysis/passes/framepointer)
Requires:       go(golang.org/x/tools/go/analysis/passes/hostport)
Requires:       go(golang.org/x/tools/go/analysis/passes/httpmux)
Requires:       go(golang.org/x/tools/go/analysis/passes/httpresponse)
Requires:       go(golang.org/x/tools/go/analysis/passes/ifaceassert)
Requires:       go(golang.org/x/tools/go/analysis/passes/inline)
Requires:       go(golang.org/x/tools/go/analysis/passes/inspect)
Requires:       go(golang.org/x/tools/go/analysis/passes/loopclosure)
Requires:       go(golang.org/x/tools/go/analysis/passes/lostcancel)
Requires:       go(golang.org/x/tools/go/analysis/passes/modernize)
Requires:       go(golang.org/x/tools/go/analysis/passes/nilfunc)
Requires:       go(golang.org/x/tools/go/analysis/passes/nilness)
Requires:       go(golang.org/x/tools/go/analysis/passes/pkgfact)
Requires:       go(golang.org/x/tools/go/analysis/passes/printf)
Requires:       go(golang.org/x/tools/go/analysis/passes/reflectvaluecompare)
Requires:       go(golang.org/x/tools/go/analysis/passes/shadow)
Requires:       go(golang.org/x/tools/go/analysis/passes/shift)
Requires:       go(golang.org/x/tools/go/analysis/passes/sigchanyzer)
Requires:       go(golang.org/x/tools/go/analysis/passes/slog)
Requires:       go(golang.org/x/tools/go/analysis/passes/sortslice)
Requires:       go(golang.org/x/tools/go/analysis/passes/stdmethods)
Requires:       go(golang.org/x/tools/go/analysis/passes/stdversion)
Requires:       go(golang.org/x/tools/go/analysis/passes/stringintconv)
Requires:       go(golang.org/x/tools/go/analysis/passes/structtag)
Requires:       go(golang.org/x/tools/go/analysis/passes/testinggoroutine)
Requires:       go(golang.org/x/tools/go/analysis/passes/tests)
Requires:       go(golang.org/x/tools/go/analysis/passes/timeformat)
Requires:       go(golang.org/x/tools/go/analysis/passes/unmarshal)
Requires:       go(golang.org/x/tools/go/analysis/passes/unreachable)
Requires:       go(golang.org/x/tools/go/analysis/passes/unsafeptr)
Requires:       go(golang.org/x/tools/go/analysis/passes/unusedresult)
Requires:       go(golang.org/x/tools/go/analysis/passes/unusedwrite)
Requires:       go(golang.org/x/tools/go/analysis/passes/waitgroup)
Requires:       go(golang.org/x/tools/go/ast/inspector)
Requires:       go(golang.org/x/tools/go/gcexportdata)
Requires:       go(golang.org/x/tools/go/packages)
Requires:       go(golang.org/x/tools/go/types/objectpath)
Requires:       go(golang.org/x/tools/imports)
Requires:       go(honnef.co/go/tools/analysis/facts/directives)
Requires:       go(honnef.co/go/tools/analysis/facts/generated)
Requires:       go(honnef.co/go/tools/analysis/lint)
Requires:       go(honnef.co/go/tools/config)
Requires:       go(honnef.co/go/tools/quickfix)
Requires:       go(honnef.co/go/tools/simple)
Requires:       go(honnef.co/go/tools/staticcheck)
Requires:       go(honnef.co/go/tools/stylecheck)
Requires:       go(honnef.co/go/tools/unused)
Requires:       go(mvdan.cc/gofumpt/format)
Requires:       go(mvdan.cc/unparam/check)

%description
Go linter aggregation and integration libraries. This package contains the
complete upstream repository sources and tests.

# Nested modules use their declared import paths in the GOPATH test tree.
%check -p
%go_common
mkdir -p %{_builddir}/go/src/github.com/golangci/docs
cp -a docs/. %{_builddir}/go/src/github.com/golangci/docs/

# Build the test driver once in GOPATH mode. The test helper otherwise
# invokes make and re-enables network module resolution.
export GOLANGCI_LINT_INSTALLED=true
mkdir -p %{_builddir}/go/src/%{go_import_path}
cp -a . %{_builddir}/go/src/%{go_import_path}/
pushd %{_builddir}/go/src/%{go_import_path}
%{__go} build -o golangci-lint ./cmd/golangci-lint
popd

# Install independent module roots at their real import paths.
%install -a
mkdir -p %{buildroot}%{go_sys_gopath}/github.com/golangci/docs
cp -a docs/. %{buildroot}%{go_sys_gopath}/github.com/golangci/docs/

# Exercise every non-fixture nested module as well as the root module.
%check -a
%go_common
pushd %{_builddir}/go/src/github.com/golangci/golangci-lint/v2/scripts/gen_github_action_config
%{__go} test %{go_test_flags_default} ./...
popd

# docs/go.mod has no active Go packages; retain its sources and dependencies.

%files
%doc README.md
%license LICENSE
%license internal/go/LICENSE
%license internal/x/LICENSE
%license pkg/goformatters/gci/internal/LICENSE
%license third_party/dogsled/LICENSE
%license third_party/gochecknoglobals/LICENSE
%license third_party/gochecknoinits/LICENSE
%license third_party/gometalinter/LICENSE
%license third_party/lll/LICENSE
%license third_party/nakedret/LICENSE
%license third_party/x_tools/LICENSE
%{go_sys_gopath}/%{go_import_path}
%{go_sys_gopath}/github.com/golangci/docs

%changelog
%autochangelog
