# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name profiling
%global full_version 1.0.18
%global pkgname profiling-1

Name:           rust-profiling-1
Version:        1.0.18
Release:        %autorelease
Summary:        Rust crate "profiling"
License:        MIT OR Apache-2.0
URL:            https://github.com/aclysma/profiling
#!RemoteAsset:  sha256:3d595e54a326bc53c1c197b32d295e14b169e3cfeaa8dc82b529f947fba6bcf5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/type-check) = %{version}

%description
Source code for takopackized Rust crate "profiling"

%package     -n %{name}+optick
Summary:        Very thin abstraction over other profiler crates - feature "optick"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(optick-1/default) >= 1.3.0
Provides:       crate(%{pkgname}/optick) = %{version}

%description -n %{name}+optick
This metapackage enables feature "optick" for the Rust profiling crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+profile-with-optick
Summary:        Very thin abstraction over other profiler crates - feature "profile-with-optick"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/optick) = %{version}
Requires:       crate(profiling-procmacros-1/profile-with-optick) >= 1.0.18
Provides:       crate(%{pkgname}/profile-with-optick) = %{version}

%description -n %{name}+profile-with-optick
This metapackage enables feature "profile-with-optick" for the Rust profiling crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+profile-with-puffin
Summary:        Very thin abstraction over other profiler crates - feature "profile-with-puffin"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/puffin) = %{version}
Requires:       crate(profiling-procmacros-1/profile-with-puffin) >= 1.0.18
Provides:       crate(%{pkgname}/profile-with-puffin) = %{version}

%description -n %{name}+profile-with-puffin
This metapackage enables feature "profile-with-puffin" for the Rust profiling crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+profile-with-superluminal
Summary:        Very thin abstraction over other profiler crates - feature "profile-with-superluminal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/superluminal-perf) = %{version}
Requires:       crate(profiling-procmacros-1/profile-with-superluminal) >= 1.0.18
Provides:       crate(%{pkgname}/profile-with-superluminal) = %{version}

%description -n %{name}+profile-with-superluminal
This metapackage enables feature "profile-with-superluminal" for the Rust profiling crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+profile-with-tracing
Summary:        Very thin abstraction over other profiler crates - feature "profile-with-tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tracing) = %{version}
Requires:       crate(profiling-procmacros-1/profile-with-tracing) >= 1.0.18
Provides:       crate(%{pkgname}/profile-with-tracing) = %{version}

%description -n %{name}+profile-with-tracing
This metapackage enables feature "profile-with-tracing" for the Rust profiling crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+profile-with-tracy
Summary:        Very thin abstraction over other profiler crates - feature "profile-with-tracy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tracy-client) = %{version}
Requires:       crate(profiling-procmacros-1/profile-with-tracy) >= 1.0.18
Provides:       crate(%{pkgname}/profile-with-tracy) = %{version}

%description -n %{name}+profile-with-tracy
This metapackage enables feature "profile-with-tracy" for the Rust profiling crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+profiling-procmacros
Summary:        Very thin abstraction over other profiler crates - feature "profiling-procmacros" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(profiling-procmacros-1/default) >= 1.0.18
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/procmacros) = %{version}
Provides:       crate(%{pkgname}/profiling-procmacros) = %{version}

%description -n %{name}+profiling-procmacros
This metapackage enables feature "profiling-procmacros" for the Rust profiling crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "procmacros" features.

%package     -n %{name}+puffin
Summary:        Very thin abstraction over other profiler crates - feature "puffin"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(puffin-0.20/default) >= 0.20.0
Provides:       crate(%{pkgname}/puffin) = %{version}

%description -n %{name}+puffin
This metapackage enables feature "puffin" for the Rust profiling crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+superluminal-perf
Summary:        Very thin abstraction over other profiler crates - feature "superluminal-perf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(superluminal-perf-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/superluminal-perf) = %{version}

%description -n %{name}+superluminal-perf
This metapackage enables feature "superluminal-perf" for the Rust profiling crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Very thin abstraction over other profiler crates - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust profiling crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracy-client
Summary:        Very thin abstraction over other profiler crates - feature "tracy-client"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracy-client-0.18/default) >= 0.18.0
Provides:       crate(%{pkgname}/tracy-client) = %{version}

%description -n %{name}+tracy-client
This metapackage enables feature "tracy-client" for the Rust profiling crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
