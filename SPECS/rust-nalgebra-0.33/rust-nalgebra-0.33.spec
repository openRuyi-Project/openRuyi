# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name nalgebra
%global full_version 0.33.3
%global pkgname nalgebra-0.33

Name:           rust-nalgebra-0.33
Version:        0.33.3
Release:        %autorelease
Summary:        Rust crate "nalgebra"
License:        Apache-2.0
URL:            https://nalgebra.org
#!RemoteAsset:  sha256:9d43ddcacf343185dfd6de2ee786d9e8b1c2301622afab66b6c73baf9882abfd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(approx-0.5) >= 0.5.0
Requires:       crate(num-complex-0.4) >= 0.4.0
Requires:       crate(num-rational-0.4) >= 0.4.0
Requires:       crate(num-traits-0.2) >= 0.2.0
Requires:       crate(simba-0.9) >= 0.9.0
Requires:       crate(typenum-1/default) >= 1.12.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/slow-tests) = %{version}
Provides:       crate(%{pkgname}/sparse) = %{version}

%description
Source code for takopackized Rust crate "nalgebra"

%package     -n %{name}+alga
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "alga"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(alga-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/alga) = %{version}

%description -n %{name}+alga
This metapackage enables feature "alga" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytemuck
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "bytemuck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytemuck-1/default) >= 1.5.0
Provides:       crate(%{pkgname}/bytemuck) = %{version}

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+convert-bytemuck
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "convert-bytemuck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bytemuck) = %{version}
Requires:       crate(num-complex-0.4/bytemuck) >= 0.4.0
Provides:       crate(%{pkgname}/convert-bytemuck) = %{version}

%description -n %{name}+convert-bytemuck
This metapackage enables feature "convert-bytemuck" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+debug
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rand) = %{version}
Requires:       crate(approx-0.5/num-complex) >= 0.5.0
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/macros) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+glam014
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam014" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glam-0.14/default) >= 0.14.0
Provides:       crate(%{pkgname}/convert-glam014) = %{version}
Provides:       crate(%{pkgname}/glam014) = %{version}

%description -n %{name}+glam014
This metapackage enables feature "glam014" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam014" feature.

%package     -n %{name}+glam015
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam015" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glam-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname}/convert-glam015) = %{version}
Provides:       crate(%{pkgname}/glam015) = %{version}

%description -n %{name}+glam015
This metapackage enables feature "glam015" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam015" feature.

%package     -n %{name}+glam016
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam016" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glam-0.16/default) >= 0.16.0
Provides:       crate(%{pkgname}/convert-glam016) = %{version}
Provides:       crate(%{pkgname}/glam016) = %{version}

%description -n %{name}+glam016
This metapackage enables feature "glam016" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam016" feature.

%package     -n %{name}+glam017
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam017" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glam-0.17/default) >= 0.17.0
Provides:       crate(%{pkgname}/convert-glam017) = %{version}
Provides:       crate(%{pkgname}/glam017) = %{version}

%description -n %{name}+glam017
This metapackage enables feature "glam017" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam017" feature.

%package     -n %{name}+glam018
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam018" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glam-0.18/default) >= 0.18.0
Provides:       crate(%{pkgname}/convert-glam018) = %{version}
Provides:       crate(%{pkgname}/glam018) = %{version}

%description -n %{name}+glam018
This metapackage enables feature "glam018" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam018" feature.

%package     -n %{name}+glam019
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam019" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glam-0.19/default) >= 0.19.0
Provides:       crate(%{pkgname}/convert-glam019) = %{version}
Provides:       crate(%{pkgname}/glam019) = %{version}

%description -n %{name}+glam019
This metapackage enables feature "glam019" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam019" feature.

%package     -n %{name}+glam020
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam020" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glam-0.20/default) >= 0.20.0
Provides:       crate(%{pkgname}/convert-glam020) = %{version}
Provides:       crate(%{pkgname}/glam020) = %{version}

%description -n %{name}+glam020
This metapackage enables feature "glam020" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam020" feature.

%package     -n %{name}+glam021
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam021" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glam-0.21/default) >= 0.21.0
Provides:       crate(%{pkgname}/convert-glam021) = %{version}
Provides:       crate(%{pkgname}/glam021) = %{version}

%description -n %{name}+glam021
This metapackage enables feature "glam021" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam021" feature.

%package     -n %{name}+glam022
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam022" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glam-0.22/default) >= 0.22.0
Provides:       crate(%{pkgname}/convert-glam022) = %{version}
Provides:       crate(%{pkgname}/glam022) = %{version}

%description -n %{name}+glam022
This metapackage enables feature "glam022" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam022" feature.

%package     -n %{name}+glam023
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam023" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glam-0.23/default) >= 0.23.0
Provides:       crate(%{pkgname}/convert-glam023) = %{version}
Provides:       crate(%{pkgname}/glam023) = %{version}

%description -n %{name}+glam023
This metapackage enables feature "glam023" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam023" feature.

%package     -n %{name}+glam024
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam024" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glam-0.24/default) >= 0.24.0
Provides:       crate(%{pkgname}/convert-glam024) = %{version}
Provides:       crate(%{pkgname}/glam024) = %{version}

%description -n %{name}+glam024
This metapackage enables feature "glam024" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam024" feature.

%package     -n %{name}+glam025
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam025" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glam-0.25/default) >= 0.25.0
Provides:       crate(%{pkgname}/convert-glam025) = %{version}
Provides:       crate(%{pkgname}/glam025) = %{version}

%description -n %{name}+glam025
This metapackage enables feature "glam025" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam025" feature.

%package     -n %{name}+glam027
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam027" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glam-0.27/default) >= 0.27.0
Provides:       crate(%{pkgname}/convert-glam027) = %{version}
Provides:       crate(%{pkgname}/glam027) = %{version}

%description -n %{name}+glam027
This metapackage enables feature "glam027" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam027" feature.

%package     -n %{name}+glam028
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam028" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glam-0.28/default) >= 0.28.0
Provides:       crate(%{pkgname}/convert-glam028) = %{version}
Provides:       crate(%{pkgname}/glam028) = %{version}

%description -n %{name}+glam028
This metapackage enables feature "glam028" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam028" feature.

%package     -n %{name}+glam029
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam029" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glam-0.29/default) >= 0.29.0
Provides:       crate(%{pkgname}/convert-glam029) = %{version}
Provides:       crate(%{pkgname}/glam029) = %{version}

%description -n %{name}+glam029
This metapackage enables feature "glam029" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam029" feature.

%package     -n %{name}+glam030
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam030" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glam-0.30/default) >= 0.30.0
Provides:       crate(%{pkgname}/convert-glam030) = %{version}
Provides:       crate(%{pkgname}/glam030) = %{version}

%description -n %{name}+glam030
This metapackage enables feature "glam030" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam030" feature.

%package     -n %{name}+io
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pest) = %{version}
Requires:       crate(%{pkgname}/pest-derive) = %{version}
Provides:       crate(%{pkgname}/io) = %{version}

%description -n %{name}+io
This metapackage enables feature "io" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libm
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "libm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(simba-0.9/libm) >= 0.9.0
Provides:       crate(%{pkgname}/libm) = %{version}

%description -n %{name}+libm
This metapackage enables feature "libm" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libm-force
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "libm-force"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(simba-0.9/libm-force) >= 0.9.0
Provides:       crate(%{pkgname}/libm-force) = %{version}

%description -n %{name}+libm-force
This metapackage enables feature "libm-force" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+matrixcompare-core
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "matrixcompare-core" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(matrixcompare-core-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/compare) = %{version}
Provides:       crate(%{pkgname}/matrixcompare-core) = %{version}

%description -n %{name}+matrixcompare-core
This metapackage enables feature "matrixcompare-core" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "compare" feature.

%package     -n %{name}+matrixmultiply
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "matrixmultiply"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(matrixmultiply-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/matrixmultiply) = %{version}

%description -n %{name}+matrixmultiply
This metapackage enables feature "matrixmultiply" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mint
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "mint" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mint-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/convert-mint) = %{version}
Provides:       crate(%{pkgname}/mint) = %{version}

%description -n %{name}+mint
This metapackage enables feature "mint" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-mint" feature.

%package     -n %{name}+nalgebra-macros
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "nalgebra-macros" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(nalgebra-macros-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname}/macros) = %{version}
Provides:       crate(%{pkgname}/nalgebra-macros) = %{version}

%description -n %{name}+nalgebra-macros
This metapackage enables feature "nalgebra-macros" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "macros" feature.

%package     -n %{name}+pest
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "pest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pest-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/pest) = %{version}

%description -n %{name}+pest
This metapackage enables feature "pest" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pest-derive
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "pest_derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pest-derive-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/pest-derive) = %{version}

%description -n %{name}+pest-derive
This metapackage enables feature "pest_derive" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proptest
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "proptest" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proptest-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/proptest) = %{version}
Provides:       crate(%{pkgname}/proptest-support) = %{version}

%description -n %{name}+proptest
This metapackage enables feature "proptest" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "proptest-support" feature.

%package     -n %{name}+quickcheck
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "quickcheck" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quickcheck-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}
Provides:       crate(%{pkgname}/quickcheck) = %{version}

%description -n %{name}+quickcheck
This metapackage enables feature "quickcheck" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "arbitrary" feature.

%package     -n %{name}+rand
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "rand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rand-distr) = %{version}
Requires:       crate(%{pkgname}/rand-no-std) = %{version}
Requires:       crate(rand-0.8/std) >= 0.8.0
Requires:       crate(rand-0.8/std-rng) >= 0.8.0
Provides:       crate(%{pkgname}/rand) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-package
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "rand-package" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/rand-no-std) = %{version}
Provides:       crate(%{pkgname}/rand-package) = %{version}

%description -n %{name}+rand-package
This metapackage enables feature "rand-package" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rand-no-std" feature.

%package     -n %{name}+rand-distr
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "rand_distr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-distr-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/rand-distr) = %{version}

%description -n %{name}+rand-distr
This metapackage enables feature "rand_distr" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "rayon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rayon-1/default) >= 1.6.0
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "rkyv"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rkyv-0.7) >= 0.7.41
Provides:       crate(%{pkgname}/rkyv) = %{version}

%description -n %{name}+rkyv
This metapackage enables feature "rkyv" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv-safe-deser
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "rkyv-safe-deser"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rkyv-serialize) = %{version}
Requires:       crate(rkyv-0.7/validation) >= 0.7.41
Provides:       crate(%{pkgname}/rkyv-safe-deser) = %{version}

%description -n %{name}+rkyv-safe-deser
This metapackage enables feature "rkyv-safe-deser" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv-serialize
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "rkyv-serialize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rkyv-serialize-no-std) = %{version}
Requires:       crate(rkyv-0.7/std) >= 0.7.41
Requires:       crate(rkyv-0.7/validation) >= 0.7.41
Provides:       crate(%{pkgname}/rkyv-serialize) = %{version}

%description -n %{name}+rkyv-serialize
This metapackage enables feature "rkyv-serialize" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv-serialize-no-std
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "rkyv-serialize-no-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rkyv-0.7/size-32) >= 0.7.41
Provides:       crate(%{pkgname}/rkyv-serialize-no-std) = %{version}

%description -n %{name}+rkyv-serialize-no-std
This metapackage enables feature "rkyv-serialize-no-std" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-serialize
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "serde-serialize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde-serialize-no-std) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/serde-serialize) = %{version}

%description -n %{name}+serde-serialize
This metapackage enables feature "serde-serialize" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-serialize-no-std
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "serde-serialize-no-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(num-complex-0.4/serde) >= 0.4.0
Provides:       crate(%{pkgname}/serde-serialize-no-std) = %{version}

%description -n %{name}+serde-serialize-no-std
This metapackage enables feature "serde-serialize-no-std" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/matrixmultiply) = %{version}
Requires:       crate(approx-0.5/std) >= 0.5.0
Requires:       crate(num-complex-0.4/std) >= 0.4.0
Requires:       crate(num-rational-0.4/std) >= 0.4.0
Requires:       crate(num-traits-0.2/std) >= 0.2.0
Requires:       crate(simba-0.9/std) >= 0.9.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
