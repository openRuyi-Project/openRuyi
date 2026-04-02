# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name prodash
%global full_version 30.0.1
%global pkgname prodash-30.0

Name:           rust-prodash-30.0
Version:        30.0.1
Release:        %autorelease
Summary:        Rust crate "prodash"
License:        MIT
URL:            https://github.com/GitoxideLabs/prodash
#!RemoteAsset:  sha256:5a6efc566849d3d9d737c5cb06cc50e48950ebe3d3f9d70631490fff3a07b139
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "prodash"

%package     -n %{name}+async-io
Summary:        Dashboard for visualizing progress of asynchronous and possibly blocking tasks - feature "async-io"
Requires:       crate(%{pkgname})
Requires:       crate(async-io-2.0/default) >= 2.2.1
Provides:       crate(%{pkgname}/async-io)

%description -n %{name}+async-io
This metapackage enables feature "async-io" for the Rust prodash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytesize
Summary:        Dashboard for visualizing progress of asynchronous and possibly blocking tasks - feature "bytesize" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(bytesize-2.0/default) >= 2.0.1
Provides:       crate(%{pkgname}/bytesize)
Provides:       crate(%{pkgname}/unit-bytes)

%description -n %{name}+bytesize
This metapackage enables feature "bytesize" for the Rust prodash crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unit-bytes" feature.

%package     -n %{name}+crosstermion
Summary:        Dashboard for visualizing progress of asynchronous and possibly blocking tasks - feature "crosstermion"
Requires:       crate(%{pkgname})
Requires:       crate(crosstermion-0.14) >= 0.14.0
Provides:       crate(%{pkgname}/crosstermion)

%description -n %{name}+crosstermion
This metapackage enables feature "crosstermion" for the Rust prodash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ctrlc
Summary:        Dashboard for visualizing progress of asynchronous and possibly blocking tasks - feature "ctrlc"
Requires:       crate(%{pkgname})
Requires:       crate(ctrlc-3.0/termination) >= 3.1.4
Provides:       crate(%{pkgname}/ctrlc)

%description -n %{name}+ctrlc
This metapackage enables feature "ctrlc" for the Rust prodash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dashmap
Summary:        Dashboard for visualizing progress of asynchronous and possibly blocking tasks - feature "dashmap" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(dashmap-6.0) >= 6.0.1
Provides:       crate(%{pkgname}/dashmap)
Provides:       crate(%{pkgname}/progress-tree-hp-hashmap)

%description -n %{name}+dashmap
This metapackage enables feature "dashmap" for the Rust prodash crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "progress-tree-hp-hashmap" feature.

%package     -n %{name}+futures-core
Summary:        Dashboard for visualizing progress of asynchronous and possibly blocking tasks - feature "futures-core"
Requires:       crate(%{pkgname})
Requires:       crate(futures-core-0.3) >= 0.3.4
Provides:       crate(%{pkgname}/futures-core)

%description -n %{name}+futures-core
This metapackage enables feature "futures-core" for the Rust prodash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-lite
Summary:        Dashboard for visualizing progress of asynchronous and possibly blocking tasks - feature "futures-lite"
Requires:       crate(%{pkgname})
Requires:       crate(futures-lite-2.0/default) >= 2.1.0
Provides:       crate(%{pkgname}/futures-lite)

%description -n %{name}+futures-lite
This metapackage enables feature "futures-lite" for the Rust prodash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+human-format
Summary:        Dashboard for visualizing progress of asynchronous and possibly blocking tasks - feature "human_format" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(human-format-1.0/default) >= 1.0.3
Provides:       crate(%{pkgname}/human-format)
Provides:       crate(%{pkgname}/unit-human)

%description -n %{name}+human-format
This metapackage enables feature "human_format" for the Rust prodash crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unit-human" feature.

%package     -n %{name}+is-terminal
Summary:        Dashboard for visualizing progress of asynchronous and possibly blocking tasks - feature "is-terminal" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(is-terminal-0.4/default) >= 0.4.9
Provides:       crate(%{pkgname}/is-terminal)
Provides:       crate(%{pkgname}/render-line-autoconfigure)

%description -n %{name}+is-terminal
This metapackage enables feature "is-terminal" for the Rust prodash crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "render-line-autoconfigure" feature.

%package     -n %{name}+jiff
Summary:        Dashboard for visualizing progress of asynchronous and possibly blocking tasks - feature "jiff" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(jiff-0.2/default) >= 0.2.4
Provides:       crate(%{pkgname}/jiff)
Provides:       crate(%{pkgname}/local-time)
Provides:       crate(%{pkgname}/unit-duration)

%description -n %{name}+jiff
This metapackage enables feature "jiff" for the Rust prodash crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "local-time", and "unit-duration" features.

%package     -n %{name}+log
Summary:        Dashboard for visualizing progress of asynchronous and possibly blocking tasks - feature "log" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(log-0.4/default) >= 0.4.8
Provides:       crate(%{pkgname}/log)
Provides:       crate(%{pkgname}/progress-log)
Provides:       crate(%{pkgname}/progress-tree-log)

%description -n %{name}+log
This metapackage enables feature "log" for the Rust prodash crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "progress-log", and "progress-tree-log" features.

%package     -n %{name}+parking-lot
Summary:        Dashboard for visualizing progress of asynchronous and possibly blocking tasks - feature "parking_lot" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(parking-lot-0.12) >= 0.12.5
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/parking-lot)
Provides:       crate(%{pkgname}/progress-tree)

%description -n %{name}+parking-lot
This metapackage enables feature "parking_lot" for the Rust prodash crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "progress-tree" features.

%package     -n %{name}+render-line
Summary:        Dashboard for visualizing progress of asynchronous and possibly blocking tasks - feature "render-line"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/jiff)
Requires:       crate(%{pkgname}/unicode-width)
Requires:       crate(crosstermion-0.14/color) >= 0.14.0
Provides:       crate(%{pkgname}/render-line)

%description -n %{name}+render-line
This metapackage enables feature "render-line" for the Rust prodash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+render-line-crossterm
Summary:        Dashboard for visualizing progress of asynchronous and possibly blocking tasks - feature "render-line-crossterm"
Requires:       crate(%{pkgname})
Requires:       crate(crosstermion-0.14/crossterm) >= 0.14.0
Provides:       crate(%{pkgname}/render-line-crossterm)

%description -n %{name}+render-line-crossterm
This metapackage enables feature "render-line-crossterm" for the Rust prodash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+render-tui
Summary:        Dashboard for visualizing progress of asynchronous and possibly blocking tasks - feature "render-tui"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/async-io)
Requires:       crate(%{pkgname}/futures-core)
Requires:       crate(%{pkgname}/futures-lite)
Requires:       crate(%{pkgname}/jiff)
Requires:       crate(%{pkgname}/tui)
Requires:       crate(%{pkgname}/tui-react)
Requires:       crate(%{pkgname}/unicode-segmentation)
Requires:       crate(%{pkgname}/unicode-width)
Requires:       crate(crosstermion-0.14/input-async) >= 0.14.0
Provides:       crate(%{pkgname}/render-tui)

%description -n %{name}+render-tui
This metapackage enables feature "render-tui" for the Rust prodash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+render-tui-crossterm
Summary:        Dashboard for visualizing progress of asynchronous and possibly blocking tasks - feature "render-tui-crossterm"
Requires:       crate(%{pkgname})
Requires:       crate(crosstermion-0.14/input-async-crossterm) >= 0.14.0
Requires:       crate(crosstermion-0.14/tui-react-crossterm) >= 0.14.0
Provides:       crate(%{pkgname}/render-tui-crossterm)

%description -n %{name}+render-tui-crossterm
This metapackage enables feature "render-tui-crossterm" for the Rust prodash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+signal-hook
Summary:        Dashboard for visualizing progress of asynchronous and possibly blocking tasks - feature "signal-hook"
Requires:       crate(%{pkgname})
Requires:       crate(signal-hook-0.3) >= 0.3.9
Provides:       crate(%{pkgname}/signal-hook)

%description -n %{name}+signal-hook
This metapackage enables feature "signal-hook" for the Rust prodash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tui
Summary:        Dashboard for visualizing progress of asynchronous and possibly blocking tasks - feature "tui"
Requires:       crate(%{pkgname})
Requires:       crate(ratatui-0.26) >= 0.26.0
Provides:       crate(%{pkgname}/tui)

%description -n %{name}+tui
This metapackage enables feature "tui" for the Rust prodash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tui-react
Summary:        Dashboard for visualizing progress of asynchronous and possibly blocking tasks - feature "tui-react"
Requires:       crate(%{pkgname})
Requires:       crate(tui-react-0.23/default) >= 0.23.0
Provides:       crate(%{pkgname}/tui-react)

%description -n %{name}+tui-react
This metapackage enables feature "tui-react" for the Rust prodash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-segmentation
Summary:        Dashboard for visualizing progress of asynchronous and possibly blocking tasks - feature "unicode-segmentation"
Requires:       crate(%{pkgname})
Requires:       crate(unicode-segmentation-1.0/default) >= 1.6.0
Provides:       crate(%{pkgname}/unicode-segmentation)

%description -n %{name}+unicode-segmentation
This metapackage enables feature "unicode-segmentation" for the Rust prodash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-width
Summary:        Dashboard for visualizing progress of asynchronous and possibly blocking tasks - feature "unicode-width"
Requires:       crate(%{pkgname})
Requires:       crate(unicode-width-0.1/default) >= 0.1.7
Provides:       crate(%{pkgname}/unicode-width)

%description -n %{name}+unicode-width
This metapackage enables feature "unicode-width" for the Rust prodash crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
