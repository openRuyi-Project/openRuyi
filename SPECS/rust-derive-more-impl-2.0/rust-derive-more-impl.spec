# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name derive_more-impl
%global full_version 2.1.1
%global pkgname derive-more-impl-2.0

Name:           rust-derive-more-impl-2.0
Version:        2.1.1
Release:        %autorelease
Summary:        Rust crate "derive_more-impl"
License:        MIT
URL:            https://github.com/JelteF/derive_more
#!RemoteAsset:  sha256:799a97264921d8623a957f6c3b9011f3b5492f557bbb7a5a19b7fa6d06ba8dcb
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(rustc-version-0.4/default) >= 0.4.1
Requires:       crate(syn-2.0/default) >= 2.0.117
Provides:       crate(derive-more-impl) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/constructor)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/deref)
Provides:       crate(%{pkgname}/deref-mut)
Provides:       crate(%{pkgname}/index)
Provides:       crate(%{pkgname}/index-mut)
Provides:       crate(%{pkgname}/into-iterator)
Provides:       crate(%{pkgname}/sum)
Provides:       crate(%{pkgname}/try-from)

%description
Source code for takopackized Rust crate "derive_more-impl"

%package     -n %{name}+add
Summary:        Internal implementation of `derive_more` crate - feature "add" and 5 more
Requires:       crate(%{pkgname})
Requires:       crate(syn-2.0/extra-traits) >= 2.0.117
Requires:       crate(syn-2.0/visit) >= 2.0.117
Provides:       crate(%{pkgname}/add)
Provides:       crate(%{pkgname}/add-assign)
Provides:       crate(%{pkgname}/as-ref)
Provides:       crate(%{pkgname}/eq)
Provides:       crate(%{pkgname}/mul)
Provides:       crate(%{pkgname}/mul-assign)

%description -n %{name}+add
This metapackage enables feature "add" for the Rust derive_more-impl crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "add_assign", "as_ref", "eq", "mul", and "mul_assign" features.

%package     -n %{name}+debug
Summary:        Internal implementation of `derive_more` crate - feature "debug"
Requires:       crate(%{pkgname})
Requires:       crate(syn-2.0/extra-traits) >= 2.0.117
Requires:       crate(unicode-xid-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname}/debug)

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust derive_more-impl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+display
Summary:        Internal implementation of `derive_more` crate - feature "display"
Requires:       crate(%{pkgname})
Requires:       crate(convert-case-0.10/default) >= 0.10.0
Requires:       crate(syn-2.0/extra-traits) >= 2.0.117
Requires:       crate(unicode-xid-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname}/display)

%description -n %{name}+display
This metapackage enables feature "display" for the Rust derive_more-impl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+error
Summary:        Internal implementation of `derive_more` crate - feature "error" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(syn-2.0/extra-traits) >= 2.0.117
Provides:       crate(%{pkgname}/error)
Provides:       crate(%{pkgname}/from)
Provides:       crate(%{pkgname}/not)

%description -n %{name}+error
This metapackage enables feature "error" for the Rust derive_more-impl crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "from", and "not" features.

%package     -n %{name}+from-str
Summary:        Internal implementation of `derive_more` crate - feature "from_str"
Requires:       crate(%{pkgname})
Requires:       crate(convert-case-0.10/default) >= 0.10.0
Requires:       crate(syn-2.0/full) >= 2.0.117
Requires:       crate(syn-2.0/visit) >= 2.0.117
Provides:       crate(%{pkgname}/from-str)

%description -n %{name}+from-str
This metapackage enables feature "from_str" for the Rust derive_more-impl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full
Summary:        Internal implementation of `derive_more` crate - feature "full"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/add)
Requires:       crate(%{pkgname}/add-assign)
Requires:       crate(%{pkgname}/as-ref)
Requires:       crate(%{pkgname}/constructor)
Requires:       crate(%{pkgname}/debug)
Requires:       crate(%{pkgname}/deref)
Requires:       crate(%{pkgname}/deref-mut)
Requires:       crate(%{pkgname}/display)
Requires:       crate(%{pkgname}/eq)
Requires:       crate(%{pkgname}/error)
Requires:       crate(%{pkgname}/from)
Requires:       crate(%{pkgname}/from-str)
Requires:       crate(%{pkgname}/index)
Requires:       crate(%{pkgname}/index-mut)
Requires:       crate(%{pkgname}/into)
Requires:       crate(%{pkgname}/into-iterator)
Requires:       crate(%{pkgname}/is-variant)
Requires:       crate(%{pkgname}/mul)
Requires:       crate(%{pkgname}/mul-assign)
Requires:       crate(%{pkgname}/not)
Requires:       crate(%{pkgname}/sum)
Requires:       crate(%{pkgname}/try-from)
Requires:       crate(%{pkgname}/try-into)
Requires:       crate(%{pkgname}/try-unwrap)
Requires:       crate(%{pkgname}/unwrap)
Provides:       crate(%{pkgname}/full)

%description -n %{name}+full
This metapackage enables feature "full" for the Rust derive_more-impl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+into
Summary:        Internal implementation of `derive_more` crate - feature "into"
Requires:       crate(%{pkgname})
Requires:       crate(syn-2.0/extra-traits) >= 2.0.117
Requires:       crate(syn-2.0/visit-mut) >= 2.0.117
Provides:       crate(%{pkgname}/into)

%description -n %{name}+into
This metapackage enables feature "into" for the Rust derive_more-impl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+is-variant
Summary:        Internal implementation of `derive_more` crate - feature "is_variant" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(convert-case-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/is-variant)
Provides:       crate(%{pkgname}/try-unwrap)
Provides:       crate(%{pkgname}/unwrap)

%description -n %{name}+is-variant
This metapackage enables feature "is_variant" for the Rust derive_more-impl crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "try_unwrap", and "unwrap" features.

%package     -n %{name}+testing-helpers
Summary:        Internal implementation of `derive_more` crate - feature "testing-helpers"
Requires:       crate(%{pkgname})
Requires:       crate(syn-2.0/full) >= 2.0.117
Provides:       crate(%{pkgname}/testing-helpers)

%description -n %{name}+testing-helpers
This metapackage enables feature "testing-helpers" for the Rust derive_more-impl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+try-into
Summary:        Internal implementation of `derive_more` crate - feature "try_into"
Requires:       crate(%{pkgname})
Requires:       crate(syn-2.0/extra-traits) >= 2.0.117
Requires:       crate(syn-2.0/full) >= 2.0.117
Requires:       crate(syn-2.0/visit-mut) >= 2.0.117
Provides:       crate(%{pkgname}/try-into)

%description -n %{name}+try-into
This metapackage enables feature "try_into" for the Rust derive_more-impl crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
