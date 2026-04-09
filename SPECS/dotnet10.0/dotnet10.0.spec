# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: gns <wangbingzhen.riscv@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0
# Originally extracted from Fedora Project
# Authors: The Fedora Project Contributors

%global toolchain clang

%define __os_install_post %{nil}
# We need to manually package debug info and sources
%undefine _debuginfo_subpackages
%undefine _build_create_debug
%undefine _enable_debug_packages

%ifarch x86_64
%global runtime_arch x64
%else
%global runtime_arch riscv64
%endif

%global dotnet_major 10.0
%global dotnet_minor 103
%global dotnet_is_latest 1

# Note: upstream can produce releases with a different tag than the SDK version
%global upstream_tag v%{dotnet_major}.%{dotnet_minor}
%global upstream_tag_without_v %{dotnet_major}.%{dotnet_minor}

# From 'release.json'. Needed for source-only builds.
# Intentionally does not feed `--release-manifest` or set `-p:officialBuildId=...`,
# So we don't set 'officialBuildId', as it breaks produced builds re-bootstrapping on RISC-V.
# Triage this if you need 'officialBuildId' in the future.
%global dotnet_sourceRepository https://github.com/dotnet/dotnet.git
%global dotnet_sourceVersion c2435c3e0f46de784341ac3ed62863ce77e117b4
# %global dotnet_officialBuildId 20260125.3

%{!?runtime_id:%global runtime_id linux-%{runtime_arch}}
%global dotnet_version %{dotnet_major}.%{dotnet_minor}
%global hostfxr_version 10.0.3
%global runtime_version 10.0.3
%global aspnetcore_runtime_version 10.0.3
%global templates_version %{aspnetcore_runtime_version}
%global sdk_version 10.0.103
%global sdk_feature_band_version %(echo %{sdk_version} | cut -d '-' -f 1 | sed -e 's|[[:digit:]][[:digit:]]$|00|')

%global use_bundled_brotli 0
%global use_bundled_libunwind 1
%global use_bundled_llvm_libunwind 1
%global use_bundled_rapidjson 0
%global use_bundled_zlib 0
%global use_lttng 1

# The tracing support in CoreCLR is optional. It has a run-time
# dependency on some additional libraries like lttng-ust. The runtime
# gracefully disables tracing if the dependencies are missing.
%global __requires_exclude_from ^(%{_libdir}/dotnet/.*/libcoreclrtraceptprovider\\.so)$

# Avoid generating provides and requires for private libraries
%global privlibs             libhostfxr
%global privlibs %{privlibs}|libclrgc
%global privlibs %{privlibs}|libclrjit
%global privlibs %{privlibs}|libcoreclr
%global privlibs %{privlibs}|libcoreclrtraceptprovider
%global privlibs %{privlibs}|libhostpolicy
%global privlibs %{privlibs}|libmscordaccore
%global privlibs %{privlibs}|libmscordbi
%global privlibs %{privlibs}|libnethost
%global privlibs %{privlibs}|libSystem.Globalization.Native
%global privlibs %{privlibs}|libSystem.IO.Compression.Native
%global privlibs %{privlibs}|libSystem.Native
%global privlibs %{privlibs}|libSystem.Net.Security.Native
%global privlibs %{privlibs}|libSystem.Security.Cryptography.Native.OpenSsl
%global __provides_exclude ^(%{privlibs})\\.so
%global __requires_exclude ^(%{privlibs})\\.so

Name:           dotnet%{dotnet_major}
Version:        %{dotnet_version}
Release:        %autorelease
Summary:        .NET %{dotnet_major} Runtime and SDK
License:        0BSD AND Apache-2.0 AND (Apache-2.0 WITH LLVM-exception) AND APSL-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause AND BSL-1.0 AND bzip2-1.0.6 AND CC0-1.0 AND CC-BY-3.0 AND CC-BY-4.0 AND CC-PDDC AND CNRI-Python AND EPL-1.0 AND GPL-2.0-only AND (GPL-2.0-only WITH GCC-exception-2.0) AND GPL-2.0-or-later AND GPL-3.0-only AND ICU AND ISC AND LGPL-2.1-only AND LGPL-2.1-or-later AND LicenseRef-openRuyi-Public-Domain AND LicenseRef-ISO-8879 AND MIT AND MIT-Wu AND MS-PL AND MS-RL AND NCSA AND OFL-1.1 AND OpenSSL AND Unicode-DFS-2015 AND Unicode-DFS-2016 AND W3C-19980720 AND X11 AND Zlib
URL:            https://dotnet.microsoft.com
VCS:            git:https://github.com/dotnet/dotnet.git
#!RemoteAsset
Source0:        https://github.com/dotnet/dotnet/archive/refs/tags/%{upstream_tag}.tar.gz#/dotnet-%{sdk_version}.tar.gz
#!RemoteAsset
Source1:        https://github.com/dotnet/dotnet/releases/download/%{upstream_tag}/release.json

# Fix an error caused by fortify CFLAGS with how .NET builds some assembly files
Patch0:         runtime-disable-fortify-on-ilasm-parser.patch

ExclusiveArch:  riscv64 x86_64

BuildRequires:  aspnetcore-runtime-%{dotnet_major}
BuildRequires:  aspnetcore-targeting-pack-%{dotnet_major}
BuildRequires:  bash-completion
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  coreutils
BuildRequires:  dotnet-apphost-pack-%{dotnet_major}
BuildRequires:  dotnet-host
BuildRequires:  dotnet-hostfxr-%{dotnet_major}
BuildRequires:  dotnet-runtime-%{dotnet_major}
BuildRequires:  dotnet-sdk-%{dotnet_major}
BuildRequires:  dotnet-sdk-%{dotnet_major}-source-built-artifacts
BuildRequires:  dotnet-targeting-pack-%{dotnet_major}
BuildRequires:  dotnet-templates-%{dotnet_major}
BuildRequires:  findutils
BuildRequires:  git
BuildRequires:  gnupg
BuildRequires:  hostname
BuildRequires:  lld
BuildRequires:  lldb
BuildRequires:  llvm
%if ! %{use_bundled_llvm_libunwind}
BuildRequires:  llvm-libunwind-devel
%endif
BuildRequires:  make
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
%if ! %{use_bundled_brotli}
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libbrotlienc)
%endif
BuildRequires:  pkgconfig(krb5)
%if ! %{use_bundled_libunwind}
BuildRequires:  pkgconfig(libunwind)
%endif
BuildRequires:  pkgconfig(lttng-ust)
BuildRequires:  pkgconfig(openssl)
%if ! %{use_bundled_rapidjson}
BuildRequires:  pkgconfig(RapidJSON)
%endif
%if ! %{use_bundled_zlib}
BuildRequires:  pkgconfig(zlib)
%endif
BuildRequires:  python3
BuildRequires:  tar
BuildRequires:  util-linux

Conflicts:      dotnet%{dotnet_major}-bin

%description
.NET is a fast, lightweight and modular platform for creating
cross platform applications that work on Linux, macOS and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.

.NET contains a runtime conforming to .NET Standards a set of
framework libraries, an SDK containing compilers and a 'dotnet'
application to drive everything.

%package     -n dotnet-host
Version:        %{runtime_version}
Summary:        .NET command line launcher
Conflicts:      dotnet-host-bin

%description -n dotnet-host
The .NET host is a command line program that runs a standalone
.NET application or launches the SDK.

.NET is a fast, lightweight and modular platform for creating
cross platform applications that work on Linux, Mac and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.

%package     -n dotnet-hostfxr-%{dotnet_major}
Version:        %{runtime_version}
Summary:        .NET command line host resolver
Conflicts:      dotnet-hostfxr-%{dotnet_major}-bin
# Theoretically any version of the host should work. But lets aim for the one
# provided by this package, or from a newer version of .NET
Requires:       dotnet-host%{?_isa} >= %{runtime_version}-%{release}

%description -n dotnet-hostfxr-%{dotnet_major}
The .NET host resolver contains the logic to resolve and select
the right version of the .NET SDK or runtime to use.

.NET is a fast, lightweight and modular platform for creating
cross platform applications that work on Linux, Mac and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.

%package     -n dotnet-runtime-%{dotnet_major}
Version:        %{runtime_version}
Summary:        .NET %{runtime_version} runtime
Requires:       dotnet-hostfxr-%{dotnet_major}%{?_isa} >= %{runtime_version}-%{release}
# libicu is dlopen()ed
Requires:       icu
Conflicts:      dotnet-runtime-%{dotnet_major}-bin

%description -n dotnet-runtime-%{dotnet_major}
The .NET runtime contains everything needed to run .NET applications.
It includes a high performance Virtual Machine as well as the framework
libraries used by .NET applications.

.NET is a fast, lightweight and modular platform for creating
cross platform applications that work on Linux, Mac and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.

%package     -n dotnet-runtime-%{dotnet_major}-debuginfo
Version:        %{runtime_version}
Summary:        Managed debug symbols NET %{dotnet_major} runtime
Requires:       dotnet-runtime-%{dotnet_major}%{?_isa} = %{runtime_version}-%{release}

%description -n dotnet-runtime-%{dotnet_major}-debuginfo
This package contains the managed symbol (pdb) files useful to debug the
managed parts of the .NET runtime itself.

%package     -n aspnetcore-runtime-%{dotnet_major}
Version:        %{runtime_version}
Summary:        ASP.NET Core %{runtime_version} runtime
Requires:       dotnet-runtime-%{dotnet_major}%{?_isa} >= %{runtime_version}-%{release}
Conflicts:      aspnetcore-runtime-%{dotnet_major}-bin

%description -n aspnetcore-runtime-%{dotnet_major}
The ASP.NET Core runtime contains everything needed to run .NET
web applications. It includes a high performance Virtual Machine as
well as the framework libraries used by .NET applications.

ASP.NET Core is a fast, lightweight and modular platform for creating
cross platform web applications that work on Linux, Mac and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.

%package     -n aspnetcore-runtime-%{dotnet_major}-debuginfo
Version:        %{aspnetcore_runtime_version}
Summary:        Managed debug symbols for the ASP.NET Core %{dotnet_major} runtime
Requires:       aspnetcore-runtime-%{dotnet_major}%{?_isa} = %{aspnetcore_runtime_version}-%{release}

%description -n aspnetcore-runtime-%{dotnet_major}-debuginfo
This package contains the managed symbol (pdb) files useful to debug the
managed parts of the ASP.NET Core runtime itself.

%package     -n dotnet-templates-%{dotnet_major}
Version:        %{runtime_version}
Summary:        .NET %{runtime_version} templates
# Theoretically any version of the host should work. But lets aim for the one
# provided by this package, or from a newer version of .NET
Requires:       dotnet-host%{?_isa} >= %{runtime_version}-%{release}
Conflicts:      dotnet-templates-%{dotnet_major}-bin

%description -n dotnet-templates-%{dotnet_major}
This package contains templates used by the .NET SDK.

.NET is a fast, lightweight and modular platform for creating
cross platform applications that work on Linux, Mac and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.

%package     -n dotnet-sdk-%{dotnet_major}
Version:        %{runtime_version}
Summary:        .NET %{runtime_version} SDK
Requires:       dotnet-runtime-%{dotnet_major}%{?_isa} >= %{runtime_version}-%{release}
Requires:       aspnetcore-runtime-%{dotnet_major}%{?_isa} >= %{runtime_version}-%{release}
Requires:       dotnet-apphost-pack-%{dotnet_major}%{?_isa} >= %{runtime_version}-%{release}
Requires:       dotnet-targeting-pack-%{dotnet_major}%{?_isa} >= %{runtime_version}-%{release}
Requires:       aspnetcore-targeting-pack-%{dotnet_major}%{?_isa} >= %{runtime_version}-%{release}
Requires:       dotnet-templates-%{dotnet_major}%{?_isa} >= %{runtime_version}-%{release}
Conflicts:      dotnet-sdk-%{dotnet_major}-bin

%description -n dotnet-sdk-%{dotnet_major}
The .NET SDK is a collection of command line applications to
create, build, publish and run .NET applications.

.NET is a fast, lightweight and modular platform for creating
cross platform applications that work on Linux, Mac and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.

%package     -n dotnet-sdk-%{dotnet_major}-debuginfo
Version:        %{sdk_version}
Summary:        Managed debug symbols for the .NET %{dotnet_major} Software Development Kit
Requires:       dotnet-sdk-%{dotnet_major}%{?_isa} = %{sdk_version}-%{release}

%description -n dotnet-sdk-%{dotnet_major}-debuginfo
This package contains the managed symbol (pdb) files useful to debug the .NET
Software Development Kit (SDK) itself.

%package     -n dotnet-sdk-aot-%{dotnet_major}
Version:        %{sdk_version}
Summary:        .NET %{dotnet_major} SDK - Native AoT Support
Requires:       dotnet-sdk-%{dotnet_major}%{?_isa} >= %{runtime_version}-%{release}
Conflicts:      dotnet-sdk-aot-%{dotnet_major}-bin
# When installing AOT support, also install all dependencies needed to build
# NativeAOT applications. AOT invokes `clang ... -lssl -lcrypto -lbrotlienc
# -lbrotlidec -lz ...`.
Requires:       clang%{?_isa}
Requires:       pkgconfig(libbrotlidec)
Requires:       pkgconfig(libbrotlienc)
Requires:       pkgconfig(openssl)
Requires:       pkgconfig(zlib)
Suggests:       lttng-ust-devel

%description -n dotnet-sdk-aot-%{dotnet_major}
This package provides Ahead-of-time (AoT) compilation support for the .NET SDK.

%package     -n dotnet-apphost-pack-%{dotnet_major}
Version:        %{runtime_version}
Summary:        Targeting Pack for .NET %{dotnet_major}
Requires:       dotnet-host%{?_isa}
Conflicts:      dotnet-apphost-pack-%{dotnet_major}-bin

%description -n dotnet-apphost-pack-%{dotnet_major}
This package provides the Apphost pack for Microsoft.NETCore.App %{dotnet_major}
that allows developers to compile against and target Microsoft.NETCore.App %{dotnet_major}
applications using the .NET SDK.

%package     -n dotnet-targeting-pack-%{dotnet_major}
Version:        %{runtime_version}
Summary:        Targeting Pack for .NET %{dotnet_major}
Requires:       dotnet-host%{?_isa}
Conflicts:      dotnet-targeting-pack-%{dotnet_major}-bin

%description -n dotnet-targeting-pack-%{dotnet_major}
This package provides a targeting pack for Microsoft.NETCore.App %{dotnet_major}
that allows developers to compile against and target Microsoft.NETCore.App %{dotnet_major}
applications using the .NET SDK.

%package     -n aspnetcore-targeting-pack-%{dotnet_major}
Version:        %{aspnetcore_runtime_version}
Summary:        Targeting Pack for .NET %{dotnet_major}
Requires:       dotnet-host%{?_isa}
Conflicts:      aspnetcore-targeting-pack-%{dotnet_major}-bin

%description -n aspnetcore-targeting-pack-%{dotnet_major}
This package provides a targeting pack for Microsoft.AspNetCore.App %{dotnet_major}
that allows developers to compile against and target Microsoft.AspNetCore.App %{dotnet_major}
applications using the .NET SDK.

%package     -n dotnet-sdk-%{dotnet_major}-source-built-artifacts
Version:        %{sdk_version}
Summary:        .NET %{dotnet_major} Source Built Artifacts
Conflicts:      dotnet-sdk-%{dotnet_major}-source-built-artifacts-bin

%description -n dotnet-sdk-%{dotnet_major}-source-built-artifacts
The .NET source-built archive is a collection of packages needed
to build the .NET SDK itself.

These are not meant for general use.

%prep
release_json_tag=$(grep tag %{SOURCE1} | cut -d: -f2 | sed -E 's/[," ]*//g')
if [[ ${release_json_tag} != %{upstream_tag} ]]; then
   echo "error: tag in release.json doesn't match tag in spec file"
   exit 1
fi

%autosetup -p1 -n dotnet-%{upstream_tag_without_v}

# Remove all prebuilts and binaries
rm -rf .dotnet/
rm -rf packages/source-built
find -type f \( \
    -iname '*.bin' -or \
    -iname '*.binlog' -or \
    -iname '*.dat' -or \
    -iname '*.db' -or \
    -iname '*.dll' -or \
    -iname '*.doc' -or \
    -iname '*.docx' -or \
    -iname '*.exe' -or \
    -iname '*.mdb' -or \
    -iname '*.mod' -or \
    -iname '*.msi' -or \
    -iname '*.netmodule' -or \
    -iname '*.nupkg' -or \
    -iname '*.o' -or \
    -iname '*.obj' -or \
    -iname '*.out' -or \
    -iname '*.p7b' -or \
    -iname '*.p7s' -or \
    -iname '*.pdb' -or \
    -iname '*.pfx' -or \
    -iname '*.so' -or \
    -iname '*.tar.gz' -or \
    -iname '*.tgz' -or \
    -iname '*.tlb' -or \
    -iname '*.winmd' -or \
    -iname '*.vsix' -or \
    -iname '*.zip' \
    \) \
    -delete

# No js/nodejs code should be getting built, and no javascript prebuilts
# packages should be present on disk or used. Delete things to make the build
# break if any Javascript is compiled/used.
find -iname package.json -delete
find -iname package-lock.json -delete
rm -rf ./src/aspnetcore/src/Components/Web.JS/dist

rm -rf .dotnet
mkdir -p prereqs/packages/archive
ln -s %{_libdir}/dotnet/source-built-artifacts/Private.SourceBuilt.Artifacts.*.tar.gz prereqs/packages/archive/

%if ! %{use_bundled_brotli}
rm -r src/runtime/src/native/external/brotli/
%endif

%if ! %{use_bundled_libunwind}
rm -r src/runtime/src/native/external/libunwind/
%endif

%if ! %{use_bundled_llvm_libunwind}
rm -r src/runtime/src/native/external/llvm-libunwind
%endif

%if ! %{use_bundled_rapidjson}
rm -r src/runtime/src/native/external/rapidjson
%endif

%if ! %{use_bundled_zlib}
rm -r src/runtime/src/native/external/zlib-ng
%endif

%build
cat /etc/os-release

# We need to create a copy because build scripts will mutate this
cp -a %{_libdir}/dotnet previously-built-dotnet
find previously-built-dotnet

%set_build_flags

# -fstack-clash-protection breaks CoreCLR
CFLAGS=$(echo $CFLAGS  | sed -e 's/-fstack-clash-protection//' )
CXXFLAGS=$(echo $CXXFLAGS  | sed -e 's/-fstack-clash-protection//' )

export EXTRA_CFLAGS="$CFLAGS"
export EXTRA_CXXFLAGS="$CXXFLAGS"
export EXTRA_LDFLAGS="$LDFLAGS"
CFLAGS=""
CXXFLAGS=""
LDFLAGS=""

# Disable tracing, which is incompatible with certain versions of
# lttng See https://github.com/dotnet/runtime/issues/57784. The
# suggested compile-time change doesn't work, unfortunately.
export COMPlus_LTTng=0

system_libs=
%if ! %{use_bundled_brotli}
    system_libs=$system_libs+brotli+
%endif
%if ! %{use_bundled_libunwind}
    system_libs=$system_libs+libunwind+
%endif
%if ! %{use_bundled_llvm_libunwind}
    system_libs=$system_libs+llvmlibunwind+
%endif
%if ! %{use_bundled_rapidjson}
    system_libs=$system_libs+rapidjson+
%endif
%if ! %{use_bundled_zlib}
    system_libs=$system_libs+zlib+
%endif
%if ! %{use_lttng}
    system_libs=$system_libs-lttng-
%endif

# Prevent stall
%ifarch riscv64
max_attempts=3
%else
max_attempts=1
%endif

function retry_until_success {
    local exit_code=1
    local tries=$1
    shift
    set +e
    while [[ $exit_code != 0 ]] && [[ $tries != 0 ]]; do
        (( tries = tries - 1 ))
        "$@"
        exit_code=$?
    done
    set -e
    return $exit_code
}

cat >dotnet-rpm-build.sh <<EOF
#!/bin/bash

set -euo pipefail
set -x

find -depth -name 'artifacts' -type d -print -exec rm -rf {} \;

./build.sh \
  --clean-while-building \
  --with-sdk previously-built-dotnet \
  --source-only \
  --source-repository %{dotnet_sourceRepository} \
  --source-version %{dotnet_sourceVersion} \
  --os linux \
  --rid linux-%{runtime_arch} \
  --arch %{runtime_arch} \
  -p:UseSystemLibs=${system_libs}
EOF

chmod +x dotnet-rpm-build.sh

VERBOSE=1 retry_until_success $max_attempts \
    timeout 8h \
    ./dotnet-rpm-build.sh

%install
install -dm 0755 %{buildroot}%{_libdir}/dotnet
find artifacts/assets/Release/
mkdir -p built-sdk
tar xf artifacts/assets/Release/dotnet-sdk-%{sdk_version}*-%{runtime_id}.tar.gz -C %{buildroot}%{_libdir}/dotnet/

# Delete bundled certificates: we want to use the system store only,
# except for when we have no other choice and ca-certificates doesn't
# provide it. Currently ca-ceritificates has no support for
# timestamping certificates (timestamp.ctl).
find %{buildroot}%{_libdir}/dotnet -name 'codesignctl.pem' -delete
if [[ $(find %{buildroot}%{_libdir}/dotnet -name '*.pem' -print | wc -l) != 1 ]]; then
    find %{buildroot}%{_libdir}/dotnet -name '*.pem' -print
    echo "too many certificate bundles"
    exit 2
fi

# Install managed symbols
tar xf artifacts/assets/Release/dotnet-symbols-sdk-%{sdk_version}*-%{runtime_id}.tar.gz \
   -C %{buildroot}%{_libdir}/dotnet/
find %{buildroot}%{_libdir}/dotnet/packs -iname '*.pdb' -delete

%if %{dotnet_is_latest}

# Install dynamic completions
install -dm 0755 %{buildroot}/%{bash_completions_dir}
install src/sdk/scripts/register-completions.bash %{buildroot}/%{bash_completions_dir}/dotnet

install -dm 0755 %{buildroot}%{_bindir}
ln -s ../../%{_libdir}/dotnet/dotnet %{buildroot}%{_bindir}/
ln -s ../../%{_libdir}/dotnet/dnx %{buildroot}%{_bindir}/

for section in 1 7; do
    install -dm 0755 %{buildroot}%{_mandir}/man${section}/
    find -iname 'dotnet*'.${section} -type f -exec cp {} %{buildroot}%{_mandir}/man${section}/ \;
done

install -dm 0755 %{buildroot}%{_sysconfdir}/dotnet
echo "%{_libdir}/dotnet" >> install_location
install install_location %{buildroot}%{_sysconfdir}/dotnet/
echo "%{_libdir}/dotnet" >> install_location_%{runtime_arch}
install install_location_%{runtime_arch} %{buildroot}%{_sysconfdir}/dotnet/
%endif

install -dm 0755 %{buildroot}%{_libdir}/dotnet/source-built-artifacts
install -m 0644 artifacts/assets/Release/Private.SourceBuilt.Artifacts.*.tar.gz %{buildroot}/%{_libdir}/dotnet/source-built-artifacts/

# Quick and dirty check for https://github.com/dotnet/source-build/issues/2731
test -f %{buildroot}%{_libdir}/dotnet/sdk/%{sdk_version}*/Sdks/Microsoft.NET.Sdk/Sdk/Sdk.props

find %{buildroot}%{_libdir}/dotnet/shared/Microsoft.NETCore.App -type f -and -not -name '*.pdb' | sed -E 's|%{buildroot}||' > dotnet-runtime-non-dbg-files
find %{buildroot}%{_libdir}/dotnet/shared/Microsoft.NETCore.App -type f -name '*.pdb'  | sed -E 's|%{buildroot}||' > dotnet-runtime-dbg-files
find %{buildroot}%{_libdir}/dotnet/shared/Microsoft.AspNetCore.App -type f -and -not -name '*.pdb'  | sed -E 's|%{buildroot}||' > aspnetcore-runtime-non-dbg-files
find %{buildroot}%{_libdir}/dotnet/shared/Microsoft.AspNetCore.App -type f -name '*.pdb' | sed -E 's|%{buildroot}||' > aspnetcore-runtime-dbg-files
find %{buildroot}%{_libdir}/dotnet/sdk -type d | tail -n +2 | sed -E 's|%{buildroot}||' | sed -E 's|^|%dir |' > dotnet-sdk-non-dbg-files
find %{buildroot}%{_libdir}/dotnet/sdk -type f -and -not -name '*.pdb' | sed -E 's|%{buildroot}||' >> dotnet-sdk-non-dbg-files
find %{buildroot}%{_libdir}/dotnet/sdk -type f -name '*.pdb'  | sed -E 's|%{buildroot}||' > dotnet-sdk-dbg-files

%if ! %{dotnet_is_latest}
# If this is an older version, self-test now, before we delete files. After we
# delete files, we will not have everything we need to self-test in %%check.
%{buildroot}%{_libdir}/dotnet/dotnet --info
%{buildroot}%{_libdir}/dotnet/dotnet --version

# Provided by dotnet-host from another SRPM
rm %{buildroot}%{_libdir}/dotnet/LICENSE.txt
rm %{buildroot}%{_libdir}/dotnet/ThirdPartyNotices.txt
rm %{buildroot}%{_libdir}/dotnet/dotnet
%endif

%check
%if %{dotnet_is_latest}
%{buildroot}%{_libdir}/dotnet/dotnet --info
%{buildroot}%{_libdir}/dotnet/dotnet --version
%endif

%if %{dotnet_is_latest}
%files -n dotnet-host
%dir %{_libdir}/dotnet
%{_libdir}/dotnet/dotnet
%{_libdir}/dotnet/dnx
%dir %{_libdir}/dotnet/host
%dir %{_libdir}/dotnet/host/fxr
%{_bindir}/dotnet
%{_bindir}/dnx
%license %{_libdir}/dotnet/LICENSE.txt
%license %{_libdir}/dotnet/ThirdPartyNotices.txt
%doc %{_mandir}/man1/dotnet*.1*
%doc %{_mandir}/man7/dotnet*.7*
%config(noreplace) %{_sysconfdir}/dotnet
%dir %{_datadir}/bash-completion
%dir %{bash_completions_dir}
%{_datadir}/bash-completion/completions/dotnet
%endif

%files -n dotnet-hostfxr-%{dotnet_major}
%dir %{_libdir}/dotnet/host/fxr
%{_libdir}/dotnet/host/fxr/%{hostfxr_version}*

%files -n dotnet-runtime-%{dotnet_major} -f dotnet-runtime-non-dbg-files
%dir %{_libdir}/dotnet/shared
%dir %{_libdir}/dotnet/shared/Microsoft.NETCore.App
%dir %{_libdir}/dotnet/shared/Microsoft.NETCore.App/%{runtime_version}*

%files -n dotnet-runtime-%{dotnet_major}-debuginfo -f dotnet-runtime-dbg-files

%files -n aspnetcore-runtime-%{dotnet_major} -f aspnetcore-runtime-non-dbg-files
%dir %{_libdir}/dotnet/shared
%dir %{_libdir}/dotnet/shared/Microsoft.AspNetCore.App
%dir %{_libdir}/dotnet/shared/Microsoft.AspNetCore.App/%{aspnetcore_runtime_version}*

%files -n aspnetcore-runtime-%{dotnet_major}-debuginfo -f aspnetcore-runtime-dbg-files

%files -n dotnet-templates-%{dotnet_major}
%dir %{_libdir}/dotnet/templates
%{_libdir}/dotnet/templates/%{templates_version}*

%files -n dotnet-sdk-%{dotnet_major} -f dotnet-sdk-non-dbg-files
%dir %{_libdir}/dotnet/sdk
%dir %{_libdir}/dotnet/sdk-manifests
%{_libdir}/dotnet/sdk-manifests/%{sdk_feature_band_version}*
%{_libdir}/dotnet/metadata
%{_libdir}/dotnet/library-packs
%dir %{_libdir}/dotnet/packs
%dir %{_libdir}/dotnet/packs/Microsoft.AspNetCore.App.Runtime.%{runtime_id}
%{_libdir}/dotnet/packs/Microsoft.AspNetCore.App.Runtime.%{runtime_id}/%{aspnetcore_runtime_version}*
%dir %{_libdir}/dotnet/packs/Microsoft.NETCore.App.Runtime.%{runtime_id}
%{_libdir}/dotnet/packs/Microsoft.NETCore.App.Runtime.%{runtime_id}/%{runtime_version}*

%files -n dotnet-sdk-%{dotnet_major}-debuginfo -f dotnet-sdk-dbg-files

%files -n dotnet-sdk-aot-%{dotnet_major}
%dir %{_libdir}/dotnet/packs
%dir %{_libdir}/dotnet/packs/runtime.%{runtime_id}.Microsoft.DotNet.ILCompiler/
%{_libdir}/dotnet/packs/runtime.%{runtime_id}.Microsoft.DotNet.ILCompiler/%{runtime_version}*
%dir %{_libdir}/dotnet/packs/Microsoft.NETCore.App.Runtime.NativeAOT.%{runtime_id}/
%{_libdir}/dotnet/packs/Microsoft.NETCore.App.Runtime.NativeAOT.%{runtime_id}/%{runtime_version}*
%ifarch riscv64
%dir %{_libdir}/dotnet/packs/Microsoft.NETCore.App.Crossgen2.%{runtime_id}/
%{_libdir}/dotnet/packs/Microsoft.NETCore.App.Crossgen2.%{runtime_id}/%{runtime_version}*
%endif

%files -n dotnet-apphost-pack-%{dotnet_major}
%dir %{_libdir}/dotnet/packs
%{_libdir}/dotnet/packs/Microsoft.NETCore.App.Host.%{runtime_id}

%files -n dotnet-targeting-pack-%{dotnet_major}
%dir %{_libdir}/dotnet/packs
%{_libdir}/dotnet/packs/Microsoft.NETCore.App.Ref

%files -n aspnetcore-targeting-pack-%{dotnet_major}
%dir %{_libdir}/dotnet/packs
%{_libdir}/dotnet/packs/Microsoft.AspNetCore.App.Ref

%files -n dotnet-sdk-%{dotnet_major}-source-built-artifacts
%dir %{_libdir}/dotnet
%{_libdir}/dotnet/source-built-artifacts

%changelog
%autochangelog
