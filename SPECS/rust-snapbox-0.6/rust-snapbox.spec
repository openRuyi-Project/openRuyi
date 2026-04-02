# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name snapbox
%global full_version 0.6.24
%global pkgname snapbox-0.6

Name:           rust-snapbox-0.6
Version:        0.6.24
Release:        %autorelease
Summary:        Rust crate "snapbox"
License:        MIT OR Apache-2.0
URL:            https://github.com/assert-rs/snapbox/
#!RemoteAsset:  sha256:6c1abc378119f77310836665f8523018532cf7e3faeb3b10b01da5a7321bf8e1
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstyle-1.0/default) >= 1.0.14
Requires:       crate(normalize-line-endings-0.3/default) >= 0.3.0
Requires:       crate(snapbox-macros-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "snapbox"

%package     -n %{name}+cmd
Summary:        Snapshot testing toolbox - feature "cmd"
Requires:       crate(%{pkgname})
Requires:       crate(libc-0.2/default) >= 0.2.176
Requires:       crate(os-pipe-1.0/default) >= 1.2
Requires:       crate(wait-timeout-0.2/default) >= 0.2.1
Requires:       crate(windows-sys-0.60/default) >= 0.60.2
Requires:       crate(windows-sys-0.60/win32-foundation) >= 0.60.2
Provides:       crate(%{pkgname}/cmd)

%description -n %{name}+cmd
This metapackage enables feature "cmd" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+color
Summary:        Snapshot testing toolbox - feature "color" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(anstream-0.6/default) >= 0.6.21
Requires:       crate(snapbox-macros-0.4/color) >= 0.4.0
Provides:       crate(%{pkgname}/color)
Provides:       crate(%{pkgname}/color-auto)

%description -n %{name}+color
This metapackage enables feature "color" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "color-auto" feature.

%package     -n %{name}+debug
Summary:        Snapshot testing toolbox - feature "debug"
Requires:       crate(%{pkgname})
Requires:       crate(backtrace-0.3/default) >= 0.3.0
Requires:       crate(snapbox-macros-0.4/debug) >= 0.4.0
Provides:       crate(%{pkgname}/debug)

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Snapshot testing toolbox - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/color-auto)
Requires:       crate(%{pkgname}/diff)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+detect-encoding
Summary:        Snapshot testing toolbox - feature "detect-encoding"
Requires:       crate(%{pkgname})
Requires:       crate(content-inspector-0.2/default) >= 0.2.4
Provides:       crate(%{pkgname}/detect-encoding)

%description -n %{name}+detect-encoding
This metapackage enables feature "detect-encoding" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+diff
Summary:        Snapshot testing toolbox - feature "diff"
Requires:       crate(%{pkgname})
Requires:       crate(similar-2.0/default) >= 2.7.0
Requires:       crate(similar-2.0/inline) >= 2.7.0
Provides:       crate(%{pkgname}/diff)

%description -n %{name}+diff
This metapackage enables feature "diff" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dir
Summary:        Snapshot testing toolbox - feature "dir" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/detect-encoding)
Requires:       crate(dunce-1.0/default) >= 1.0.5
Requires:       crate(filetime-0.2/default) >= 0.2.27
Requires:       crate(tempfile-3.0/default) >= 3.27.0
Requires:       crate(walkdir-2.0/default) >= 2.5.0
Provides:       crate(%{pkgname}/dir)
Provides:       crate(%{pkgname}/path)

%description -n %{name}+dir
This metapackage enables feature "dir" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "path" feature.

%package     -n %{name}+document-features
Summary:        Snapshot testing toolbox - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.11
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+examples
Summary:        Snapshot testing toolbox - feature "examples"
Requires:       crate(%{pkgname})
Requires:       crate(escargot-0.5/default) >= 0.5.14
Provides:       crate(%{pkgname}/examples)

%description -n %{name}+examples
This metapackage enables feature "examples" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json
Summary:        Snapshot testing toolbox - feature "json"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/structured-data)
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-json-1.0/default) >= 1.0.149
Provides:       crate(%{pkgname}/json)

%description -n %{name}+json
This metapackage enables feature "json" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regex
Summary:        Snapshot testing toolbox - feature "regex"
Requires:       crate(%{pkgname})
Requires:       crate(regex-1.0/std) >= 1.12.3
Provides:       crate(%{pkgname}/regex)

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+structured-data
Summary:        Snapshot testing toolbox - feature "structured-data"
Requires:       crate(%{pkgname})
Requires:       crate(serde-json-1.0/default) >= 1.0.149
Provides:       crate(%{pkgname}/structured-data)

%description -n %{name}+structured-data
This metapackage enables feature "structured-data" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+term-svg
Summary:        Snapshot testing toolbox - feature "term-svg"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/structured-data)
Requires:       crate(anstyle-svg-0.1/default) >= 0.1.12
Provides:       crate(%{pkgname}/term-svg)

%description -n %{name}+term-svg
This metapackage enables feature "term-svg" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
