# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name snapbox
%global full_version 1.2.2
%global pkgname snapbox-1

Name:           rust-snapbox-1
Version:        1.2.2
Release:        %autorelease
Summary:        Rust crate "snapbox"
License:        MIT OR Apache-2.0
URL:            https://github.com/assert-rs/snapbox/
#!RemoteAsset:  sha256:8de56eb4784a2c5c1efede55a0f06fbf481bc12b42b355b9525c15db1e3581a8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstyle-1/default) >= 1.0.14
Requires:       crate(normalize-line-endings-0.3/default) >= 0.3.0
Requires:       crate(snapbox-macros-1/default) >= 1.1.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "snapbox"

%package     -n %{name}+cmd
Summary:        Snapshot testing toolbox - feature "cmd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.183
Requires:       crate(os-pipe-1/default) >= 1.2.0
Requires:       crate(wait-timeout-0.2/default) >= 0.2.1
Requires:       crate(windows-sys-0.61/default) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Provides:       crate(%{pkgname}/cmd) = %{version}

%description -n %{name}+cmd
This metapackage enables feature "cmd" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+color
Summary:        Snapshot testing toolbox - feature "color" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(anstream-1/default) >= 1.0.0
Requires:       crate(snapbox-macros-1/color) >= 1.1.0
Provides:       crate(%{pkgname}/color) = %{version}
Provides:       crate(%{pkgname}/color-auto) = %{version}

%description -n %{name}+color
This metapackage enables feature "color" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "color-auto" feature.

%package     -n %{name}+debug
Summary:        Snapshot testing toolbox - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(backtrace-0.3/default) >= 0.3.0
Requires:       crate(snapbox-macros-1/debug) >= 1.1.0
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Snapshot testing toolbox - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/color-auto) = %{version}
Requires:       crate(%{pkgname}/diff) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+detect-encoding
Summary:        Snapshot testing toolbox - feature "detect-encoding"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(content-inspector-0.2/default) >= 0.2.4
Provides:       crate(%{pkgname}/detect-encoding) = %{version}

%description -n %{name}+detect-encoding
This metapackage enables feature "detect-encoding" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+diff
Summary:        Snapshot testing toolbox - feature "diff"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(similar-3/default) >= 3.0.0
Requires:       crate(similar-3/inline) >= 3.0.0
Provides:       crate(%{pkgname}/diff) = %{version}

%description -n %{name}+diff
This metapackage enables feature "diff" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dir
Summary:        Snapshot testing toolbox - feature "dir" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/detect-encoding) = %{version}
Requires:       crate(dunce-1/default) >= 1.0.0
Requires:       crate(filetime-0.2/default) >= 0.2.27
Requires:       crate(tempfile-3) >= 3.27.0
Requires:       crate(walkdir-2/default) >= 2.5.0
Provides:       crate(%{pkgname}/dir) = %{version}
Provides:       crate(%{pkgname}/path) = %{version}

%description -n %{name}+dir
This metapackage enables feature "dir" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "path" feature.

%package     -n %{name}+document-features
Summary:        Snapshot testing toolbox - feature "document-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.12
Provides:       crate(%{pkgname}/document-features) = %{version}

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+examples
Summary:        Snapshot testing toolbox - feature "examples"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(escargot-0.5/default) >= 0.5.15
Provides:       crate(%{pkgname}/examples) = %{version}

%description -n %{name}+examples
This metapackage enables feature "examples" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json
Summary:        Snapshot testing toolbox - feature "json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/structured-data) = %{version}
Requires:       crate(serde-1/default) >= 1.0.228
Requires:       crate(serde-json-1/default) >= 1.0.149
Provides:       crate(%{pkgname}/json) = %{version}

%description -n %{name}+json
This metapackage enables feature "json" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regex
Summary:        Snapshot testing toolbox - feature "regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/std) >= 1.12.3
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+structured-data
Summary:        Snapshot testing toolbox - feature "structured-data"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.149
Provides:       crate(%{pkgname}/structured-data) = %{version}

%description -n %{name}+structured-data
This metapackage enables feature "structured-data" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+term-svg
Summary:        Snapshot testing toolbox - feature "term-svg"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/structured-data) = %{version}
Requires:       crate(anstyle-svg-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/term-svg) = %{version}

%description -n %{name}+term-svg
This metapackage enables feature "term-svg" for the Rust snapbox crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
