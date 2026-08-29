# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name minijinja
%global full_version 2.20.0
%global pkgname minijinja-2

Name:           rust-minijinja-2
Version:        2.20.0
Release:        %autorelease
Summary:        Rust crate "minijinja"
License:        Apache-2.0
URL:            https://github.com/mitsuhiko/minijinja
#!RemoteAsset:  sha256:2929e494b2280e1e18959bb2e121da03347ae896896fdfaceaab43c88a02803f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memo-map-0.3/default) >= 0.3.1
Requires:       crate(serde-1/default) >= 1.0.130
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/adjacent-loop-items) = %{version}
Provides:       crate(%{pkgname}/builtins) = %{version}
Provides:       crate(%{pkgname}/debug) = %{version}
Provides:       crate(%{pkgname}/deserialization) = %{version}
Provides:       crate(%{pkgname}/fuel) = %{version}
Provides:       crate(%{pkgname}/internal-debug) = %{version}
Provides:       crate(%{pkgname}/internal-safe-search) = %{version}
Provides:       crate(%{pkgname}/key-interning) = %{version}
Provides:       crate(%{pkgname}/loader) = %{version}
Provides:       crate(%{pkgname}/loop-controls) = %{version}
Provides:       crate(%{pkgname}/macros) = %{version}
Provides:       crate(%{pkgname}/multi-template) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/std-collections) = %{version}
Provides:       crate(%{pkgname}/unstable-machinery) = %{version}

%description
Source code for takopackized Rust crate "minijinja"

%package     -n %{name}+custom-syntax
Summary:        Powerful template engine for Rust with minimal dependencies - feature "custom_syntax"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aho-corasick-1) >= 1.0.0
Provides:       crate(%{pkgname}/custom-syntax) = %{version}

%description -n %{name}+custom-syntax
This metapackage enables feature "custom_syntax" for the Rust minijinja crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Powerful template engine for Rust with minimal dependencies - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/adjacent-loop-items) = %{version}
Requires:       crate(%{pkgname}/builtins) = %{version}
Requires:       crate(%{pkgname}/debug) = %{version}
Requires:       crate(%{pkgname}/deserialization) = %{version}
Requires:       crate(%{pkgname}/macros) = %{version}
Requires:       crate(%{pkgname}/multi-template) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/std-collections) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust minijinja crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indexmap
Summary:        Powerful template engine for Rust with minimal dependencies - feature "indexmap" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/default) >= 2.2.0
Provides:       crate(%{pkgname}/indexmap) = %{version}
Provides:       crate(%{pkgname}/preserve-order) = %{version}

%description -n %{name}+indexmap
This metapackage enables feature "indexmap" for the Rust minijinja crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "preserve_order" feature.

%package     -n %{name}+percent-encoding
Summary:        Powerful template engine for Rust with minimal dependencies - feature "percent-encoding" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(percent-encoding-2/default) >= 2.2.0
Provides:       crate(%{pkgname}/percent-encoding) = %{version}
Provides:       crate(%{pkgname}/urlencode) = %{version}

%description -n %{name}+percent-encoding
This metapackage enables feature "percent-encoding" for the Rust minijinja crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "urlencode" feature.

%package     -n %{name}+serde-json
Summary:        Powerful template engine for Rust with minimal dependencies - feature "serde_json" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.68
Provides:       crate(%{pkgname}/json) = %{version}
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust minijinja crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "json" feature.

%package     -n %{name}+stacker
Summary:        Powerful template engine for Rust with minimal dependencies - feature "stacker"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(stacker-0.1/default) >= 0.1.15
Provides:       crate(%{pkgname}/stacker) = %{version}

%description -n %{name}+stacker
This metapackage enables feature "stacker" for the Rust minijinja crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicase
Summary:        Powerful template engine for Rust with minimal dependencies - feature "unicase"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicase-2/default) >= 2.6.0
Provides:       crate(%{pkgname}/unicase) = %{version}

%description -n %{name}+unicase
This metapackage enables feature "unicase" for the Rust minijinja crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode
Summary:        Powerful template engine for Rust with minimal dependencies - feature "unicode"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/unicase) = %{version}
Requires:       crate(%{pkgname}/unicode-ident) = %{version}
Provides:       crate(%{pkgname}/unicode) = %{version}

%description -n %{name}+unicode
This metapackage enables feature "unicode" for the Rust minijinja crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-ident
Summary:        Powerful template engine for Rust with minimal dependencies - feature "unicode-ident"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicode-ident-1/default) >= 1.0.5
Provides:       crate(%{pkgname}/unicode-ident) = %{version}

%description -n %{name}+unicode-ident
This metapackage enables feature "unicode-ident" for the Rust minijinja crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-machinery-serde
Summary:        Powerful template engine for Rust with minimal dependencies - feature "unstable_machinery_serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/unstable-machinery) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.130
Provides:       crate(%{pkgname}/unstable-machinery-serde) = %{version}

%description -n %{name}+unstable-machinery-serde
This metapackage enables feature "unstable_machinery_serde" for the Rust minijinja crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v-htmlescape
Summary:        Powerful template engine for Rust with minimal dependencies - feature "v_htmlescape" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(v-htmlescape-0.15/default) >= 0.15.8
Provides:       crate(%{pkgname}/speedups) = %{version}
Provides:       crate(%{pkgname}/v-htmlescape) = %{version}

%description -n %{name}+v-htmlescape
This metapackage enables feature "v_htmlescape" for the Rust minijinja crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "speedups" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
