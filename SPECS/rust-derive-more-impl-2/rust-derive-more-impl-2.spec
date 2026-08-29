# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name derive_more-impl
%global full_version 2.1.1
%global pkgname derive-more-impl-2

Name:           rust-derive-more-impl-2
Version:        2.1.1
Release:        %autorelease
Summary:        Rust crate "derive_more-impl"
License:        MIT
URL:            https://github.com/JelteF/derive_more
#!RemoteAsset:  sha256:799a97264921d8623a957f6c3b9011f3b5492f557bbb7a5a19b7fa6d06ba8dcb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(rustc-version-0.4) >= 0.4.0
Requires:       crate(syn-2/default) >= 2.0.45
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/constructor) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/deref) = %{version}
Provides:       crate(%{pkgname}/deref-mut) = %{version}
Provides:       crate(%{pkgname}/index) = %{version}
Provides:       crate(%{pkgname}/index-mut) = %{version}
Provides:       crate(%{pkgname}/into-iterator) = %{version}
Provides:       crate(%{pkgname}/sum) = %{version}
Provides:       crate(%{pkgname}/try-from) = %{version}

%description
Source code for takopackized Rust crate "derive_more-impl"

%package     -n %{name}+add
Summary:        Internal implementation of `derive_more` crate - feature "add" and 5 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syn-2/extra-traits) >= 2.0.45
Requires:       crate(syn-2/visit) >= 2.0.45
Provides:       crate(%{pkgname}/add) = %{version}
Provides:       crate(%{pkgname}/add-assign) = %{version}
Provides:       crate(%{pkgname}/as-ref) = %{version}
Provides:       crate(%{pkgname}/eq) = %{version}
Provides:       crate(%{pkgname}/mul) = %{version}
Provides:       crate(%{pkgname}/mul-assign) = %{version}

%description -n %{name}+add
This metapackage enables feature "add" for the Rust derive_more-impl crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "add_assign", "as_ref", "eq", "mul", and "mul_assign" features.

%package     -n %{name}+debug
Summary:        Internal implementation of `derive_more` crate - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syn-2/extra-traits) >= 2.0.45
Requires:       crate(unicode-xid-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust derive_more-impl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+display
Summary:        Internal implementation of `derive_more` crate - feature "display"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(convert-case-0.10/default) >= 0.10.0
Requires:       crate(syn-2/extra-traits) >= 2.0.45
Requires:       crate(unicode-xid-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname}/display) = %{version}

%description -n %{name}+display
This metapackage enables feature "display" for the Rust derive_more-impl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+error
Summary:        Internal implementation of `derive_more` crate - feature "error" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syn-2/extra-traits) >= 2.0.45
Provides:       crate(%{pkgname}/error) = %{version}
Provides:       crate(%{pkgname}/from) = %{version}
Provides:       crate(%{pkgname}/not) = %{version}

%description -n %{name}+error
This metapackage enables feature "error" for the Rust derive_more-impl crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "from", and "not" features.

%package     -n %{name}+from-str
Summary:        Internal implementation of `derive_more` crate - feature "from_str"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(convert-case-0.10/default) >= 0.10.0
Requires:       crate(syn-2/full) >= 2.0.45
Requires:       crate(syn-2/visit) >= 2.0.45
Provides:       crate(%{pkgname}/from-str) = %{version}

%description -n %{name}+from-str
This metapackage enables feature "from_str" for the Rust derive_more-impl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full
Summary:        Internal implementation of `derive_more` crate - feature "full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/add) = %{version}
Requires:       crate(%{pkgname}/add-assign) = %{version}
Requires:       crate(%{pkgname}/as-ref) = %{version}
Requires:       crate(%{pkgname}/constructor) = %{version}
Requires:       crate(%{pkgname}/debug) = %{version}
Requires:       crate(%{pkgname}/deref) = %{version}
Requires:       crate(%{pkgname}/deref-mut) = %{version}
Requires:       crate(%{pkgname}/display) = %{version}
Requires:       crate(%{pkgname}/eq) = %{version}
Requires:       crate(%{pkgname}/error) = %{version}
Requires:       crate(%{pkgname}/from) = %{version}
Requires:       crate(%{pkgname}/from-str) = %{version}
Requires:       crate(%{pkgname}/index) = %{version}
Requires:       crate(%{pkgname}/index-mut) = %{version}
Requires:       crate(%{pkgname}/into) = %{version}
Requires:       crate(%{pkgname}/into-iterator) = %{version}
Requires:       crate(%{pkgname}/is-variant) = %{version}
Requires:       crate(%{pkgname}/mul) = %{version}
Requires:       crate(%{pkgname}/mul-assign) = %{version}
Requires:       crate(%{pkgname}/not) = %{version}
Requires:       crate(%{pkgname}/sum) = %{version}
Requires:       crate(%{pkgname}/try-from) = %{version}
Requires:       crate(%{pkgname}/try-into) = %{version}
Requires:       crate(%{pkgname}/try-unwrap) = %{version}
Requires:       crate(%{pkgname}/unwrap) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}

%description -n %{name}+full
This metapackage enables feature "full" for the Rust derive_more-impl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+into
Summary:        Internal implementation of `derive_more` crate - feature "into"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syn-2/extra-traits) >= 2.0.45
Requires:       crate(syn-2/visit-mut) >= 2.0.45
Provides:       crate(%{pkgname}/into) = %{version}

%description -n %{name}+into
This metapackage enables feature "into" for the Rust derive_more-impl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+is-variant
Summary:        Internal implementation of `derive_more` crate - feature "is_variant" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(convert-case-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/is-variant) = %{version}
Provides:       crate(%{pkgname}/try-unwrap) = %{version}
Provides:       crate(%{pkgname}/unwrap) = %{version}

%description -n %{name}+is-variant
This metapackage enables feature "is_variant" for the Rust derive_more-impl crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "try_unwrap", and "unwrap" features.

%package     -n %{name}+testing-helpers
Summary:        Internal implementation of `derive_more` crate - feature "testing-helpers"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syn-2/full) >= 2.0.45
Provides:       crate(%{pkgname}/testing-helpers) = %{version}

%description -n %{name}+testing-helpers
This metapackage enables feature "testing-helpers" for the Rust derive_more-impl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+try-into
Summary:        Internal implementation of `derive_more` crate - feature "try_into"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syn-2/extra-traits) >= 2.0.45
Requires:       crate(syn-2/full) >= 2.0.45
Requires:       crate(syn-2/visit-mut) >= 2.0.45
Provides:       crate(%{pkgname}/try-into) = %{version}

%description -n %{name}+try-into
This metapackage enables feature "try_into" for the Rust derive_more-impl crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
