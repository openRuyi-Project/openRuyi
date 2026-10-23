# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           revive
%define go_import_path  github.com/mgechev/revive

Name:           go-github-mgechev-revive
Version:        1.17.1
Release:        %autorelease
Summary:        Configurable and extensible Go source code analyzer
License:        MIT
URL:            https://github.com/mgechev/revive
#!RemoteAsset:  sha256:52782382c491aacbf2074df09cbd2e5105c3c0c4fac44b3e273f616068a51d75
Source0:        https://github.com/mgechev/revive/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(4d63.com/gocheckcompilerdirectives)
BuildRequires:  go(4d63.com/gochecknoglobals)
BuildRequires:  go(charm.land/lipgloss/v2)
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
BuildRequires:  go(github.com/dave/dst)
BuildRequires:  go(github.com/denis-tingaikin/go-header)
BuildRequires:  go(github.com/dlclark/regexp2/v2)
BuildRequires:  go(github.com/ettle/strcase)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/fatih/structtag)
BuildRequires:  go(github.com/firefart/nonamedreturns)
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/fzipp/gocyclo)
BuildRequires:  go(github.com/ghostiam/protogetter)
BuildRequires:  go(github.com/go-critic/go-critic)
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
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/golangci/asciicheck)
BuildRequires:  go(github.com/golangci/canonicalheader)
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
BuildRequires:  go(github.com/google/renameio/v2)
BuildRequires:  go(github.com/gordonklaus/ineffassign)
BuildRequires:  go(github.com/gostaticanalysis/analysisutil)
BuildRequires:  go(github.com/gostaticanalysis/comment)
BuildRequires:  go(github.com/gostaticanalysis/forcetypeassert)
BuildRequires:  go(github.com/gostaticanalysis/nilerr)
BuildRequires:  go(github.com/hashicorp/go-immutable-radix/v2)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/hashicorp/golang-lru/v2)
BuildRequires:  go(github.com/hashicorp/hcl)
BuildRequires:  go(github.com/hexops/gotextdiff)
BuildRequires:  go(github.com/inconshreveable/mousetrap)
BuildRequires:  go(github.com/jgautheron/goconst)
BuildRequires:  go(github.com/jjti/go-spancheck)
BuildRequires:  go(github.com/julz/importas)
BuildRequires:  go(github.com/karamaru-alpha/copyloopvar)
BuildRequires:  go(github.com/kisielk/errcheck)
BuildRequires:  go(github.com/kkHAIKE/contextcheck)
BuildRequires:  go(github.com/kulti/thelper)
BuildRequires:  go(github.com/kunwardeep/paralleltest)
BuildRequires:  go(github.com/ldez/exptostd)
BuildRequires:  go(github.com/ldez/gomoddirectives)
BuildRequires:  go(github.com/ldez/grignotin)
BuildRequires:  go(github.com/ldez/structtags)
BuildRequires:  go(github.com/ldez/tagliatelle)
BuildRequires:  go(github.com/ldez/usetesting)
BuildRequires:  go(github.com/leonklingele/grouper)
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)
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
BuildRequires:  go(github.com/matttproud/golang_protobuf_extensions)
BuildRequires:  go(github.com/mitchellh/go-homedir)
BuildRequires:  go(github.com/mitchellh/mapstructure)
BuildRequires:  go(github.com/moricho/tparallel)
BuildRequires:  go(github.com/muesli/cancelreader)
BuildRequires:  go(github.com/nakabonne/nestif)
BuildRequires:  go(github.com/nishanths/exhaustive)
BuildRequires:  go(github.com/nishanths/predeclared)
BuildRequires:  go(github.com/nunnatsa/ginkgolinter)
BuildRequires:  go(github.com/pelletier/go-toml)
BuildRequires:  go(github.com/pelletier/go-toml/v2)
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
BuildRequires:  go(github.com/revive-lint/dots)
BuildRequires:  go(github.com/rivo/uniseg)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/ryancurrah/gomodguard)
BuildRequires:  go(github.com/ryancurrah/gomodguard/v2)
BuildRequires:  go(github.com/ryanrolds/sqlclosecheck)
BuildRequires:  go(github.com/sanposhiho/wastedassign/v2)
BuildRequires:  go(github.com/santhosh-tekuri/jsonschema/v6)
BuildRequires:  go(github.com/sashamelentyev/interfacebloat)
BuildRequires:  go(github.com/sashamelentyev/usestdlibvars)
BuildRequires:  go(github.com/securego/gosec/v2)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/sivchari/containedctx)
BuildRequires:  go(github.com/sonatard/noctx)
BuildRequires:  go(github.com/sourcegraph/go-diff)
BuildRequires:  go(github.com/spf13/afero)
BuildRequires:  go(github.com/spf13/cast)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/jwalterweatherman)
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
BuildRequires:  go(github.com/tomarrell/wrapcheck/v2)
BuildRequires:  go(github.com/tommy-muehle/go-mnd/v2)
BuildRequires:  go(github.com/ultraware/funlen)
BuildRequires:  go(github.com/ultraware/whitespace)
BuildRequires:  go(github.com/uudashr/gocognit)
BuildRequires:  go(github.com/uudashr/iface)
BuildRequires:  go(github.com/xen0n/gosmopolitan)
BuildRequires:  go(github.com/xo/terminfo)
BuildRequires:  go(github.com/yagipy/maintidx)
BuildRequires:  go(github.com/yeya24/promlinter)
BuildRequires:  go(github.com/ykadowak/zerologlint)
BuildRequires:  go(gitlab.com/bosi/decorder)
BuildRequires:  go(go-simpler.org/musttag)
BuildRequires:  go(go-simpler.org/sloglint)
BuildRequires:  go(go.augendre.info/arangolint)
BuildRequires:  go(go.augendre.info/fatcontext)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/exp/typeparams)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/telemetry)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/ini.v1)
BuildRequires:  go(gopkg.in/yaml.v2)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(honnef.co/go/tools)
BuildRequires:  go(mvdan.cc/editorconfig)
BuildRequires:  go(mvdan.cc/gofumpt)
BuildRequires:  go(mvdan.cc/sh/v3)
BuildRequires:  go(mvdan.cc/unparam)

Provides:       go(github.com/mgechev/revive) = %{version}
Provides:       go(github.com/mgechev/revive/cli) = %{version}
Provides:       go(github.com/mgechev/revive/config) = %{version}
Provides:       go(github.com/mgechev/revive/formatter) = %{version}
Provides:       go(github.com/mgechev/revive/internal/astutils) = %{version}
Provides:       go(github.com/mgechev/revive/internal/config) = %{version}
Provides:       go(github.com/mgechev/revive/internal/ifelse) = %{version}
Provides:       go(github.com/mgechev/revive/internal/rule) = %{version}
Provides:       go(github.com/mgechev/revive/internal/syncset) = %{version}
Provides:       go(github.com/mgechev/revive/internal/typeparams) = %{version}
Provides:       go(github.com/mgechev/revive/lint) = %{version}
Provides:       go(github.com/mgechev/revive/logging) = %{version}
Provides:       go(github.com/mgechev/revive/revivelib) = %{version}
Provides:       go(github.com/mgechev/revive/rule) = %{version}
Provides:       go(github.com/mgechev/revive/test) = %{version}
Provides:       go(github.com/mgechev/revive/tools) = %{version}

Requires:       go(codeberg.org/chavacava/garif)
Requires:       go(github.com/BurntSushi/toml)
Requires:       go(github.com/fatih/color)
Requires:       go(github.com/fatih/structtag)
Requires:       go(github.com/golangci/golangci-lint/v2)
Requires:       go(github.com/hashicorp/go-version)
Requires:       go(github.com/revive-lint/dots)
Requires:       go(github.com/spf13/afero)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/tools)

%description
Configurable and extensible Go source code analyzer.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n revive-%{version}

%install -a
# Nested modules use their declared import paths; keep repository fixtures intact.
install -d %{buildroot}%{go_sys_gopath}/github.com/mgechev/revive/tools
cp -a tools/. %{buildroot}%{go_sys_gopath}/github.com/mgechev/revive/tools/

%check
# Stage all modules at their declared paths before testing every package.
%{go_common}
mkdir -p %{_builddir}/go/src/github.com/mgechev/revive/tools
cp -a tools/. %{_builddir}/go/src/github.com/mgechev/revive/tools/
mkdir -p %{_builddir}/go/src/github.com/mgechev/revive
cp -a ./. %{_builddir}/go/src/github.com/mgechev/revive/
# The package list omits modules that only declare tool dependencies.
(
    cd %{_builddir}/go/src/github.com/mgechev/revive
    packages=$(go list -e -f '{{if or .GoFiles .CgoFiles .TestGoFiles .XTestGoFiles}}{{.ImportPath}}{{end}}' ./...)
    if [ -n "$packages" ]; then
        go test -v $packages
    fi
)

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/mgechev/revive

%changelog
%autochangelog
