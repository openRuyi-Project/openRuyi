# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: gns <wangbingzhen.riscv@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define __os_install_post %{nil}

%ifarch x86_64
%global runtime_arch x64
%else
%global runtime_arch riscv64
%endif

%global dotnet_major 10.0
%global dotnet_minor 100
%global dotnet_is_latest 1

%{!?runtime_id:%global runtime_id linux-%{runtime_arch}}
%global dotnet_version %{dotnet_major}.%{dotnet_minor}
%global hostfxr_version 10.0.0
%global runtime_version 10.0.0
%global aspnetcore_runtime_version 10.0.0
%global templates_version %{aspnetcore_runtime_version}
%global sdk_version 10.0.100
%global sdk_feature_band_version %(echo %{sdk_version} | cut -d '-' -f 1 | sed -e 's|[[:digit:]][[:digit:]]$|00|')

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

Name:           dotnet%{dotnet_major}-bin
Version:        %{dotnet_version}
Release:        %autorelease
Summary:        .NET %{dotnet_major} Runtime and SDK - Binary
License:        0BSD AND Apache-2.0 AND (Apache-2.0 WITH LLVM-exception) AND APSL-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause AND BSL-1.0 AND bzip2-1.0.6 AND CC0-1.0 AND CC-BY-3.0 AND CC-BY-4.0 AND CC-PDDC AND CNRI-Python AND EPL-1.0 AND GPL-2.0-only AND (GPL-2.0-only WITH GCC-exception-2.0) AND GPL-2.0-or-later AND GPL-3.0-only AND ICU AND ISC AND LGPL-2.1-only AND LGPL-2.1-or-later AND LicenseRef-Fedora-Public-Domain AND LicenseRef-ISO-8879 AND MIT AND MIT-Wu AND MS-PL AND MS-RL AND NCSA AND OFL-1.1 AND OpenSSL AND Unicode-DFS-2015 AND Unicode-DFS-2016 AND W3C-19980720 AND X11 AND Zlib
URL:            https://dotnet.microsoft.com
#!RemoteAsset
Source0:        https://oerv.ac.cn/repo_dropout/dotnet-bin/dotnet-sdk-%{version}-linux-riscv64.tar.gz
#!RemoteAsset
Source1:        https://oerv.ac.cn/repo_dropout/dotnet-bin/Private.SourceBuilt.Artifacts.%{version}-rtm.linux-riscv64.tar.gz
#!RemoteAsset
Source2:        https://oerv.ac.cn/repo_dropout/dotnet-bin/dotnet-sdk-%{version}-linux-x64.tar.gz
#!RemoteAsset
Source3:        https://oerv.ac.cn/repo_dropout/dotnet-bin/Private.SourceBuilt.Artifacts.%{version}-rtm.linux-x64.tar.gz
ExclusiveArch:  riscv64 x86_64

BuildRequires:  bash
BuildRequires:  icu
BuildRequires:  tar
BuildRequires:  gzip

%description
!!!  This is the Dotnet SDK intended for build pipelines. If you want
to install Dotnet for a development environment, you should install
'dotnet-sdk-%{dotnet_major}' instead.

%package     -n dotnet-host-bin
Version:        %{runtime_version}
Summary:        .NET command line launcher
Provides:       dotnet-host = %{version}

%description -n dotnet-host-bin
!!!  This is the Dotnet SDK intended for build pipelines. If you want
to install Dotnet for a development environment, you should install
'dotnet-host' instead.

%package     -n dotnet-hostfxr-%{dotnet_major}-bin
Version:        %{runtime_version}
Summary:        .NET command line host resolver
# Theoretically any version of the host should work. But lets aim for the one
# provided by this package, or from a newer version of .NET
Requires:       dotnet-host-bin%{?_isa} >= %{runtime_version}-%{release}
Provides:       dotnet-hostfxr-%{dotnet_major} = %{version}

%description -n dotnet-hostfxr-%{dotnet_major}-bin
!!!  This is the Dotnet SDK intended for build pipelines. If you want
to install Dotnet for a development environment, you should install
'dotnet-hostfxr-%{dotnet_major}' instead.

%package     -n dotnet-runtime-%{dotnet_major}-bin
Version:        %{runtime_version}
Summary:        .NET %{runtime_version} runtime
Requires:       dotnet-hostfxr-%{dotnet_major}-bin%{?_isa} >= %{runtime_version}-%{release}
# libicu is dlopen()ed
Requires:       icu
Provides:       dotnet-runtime-%{dotnet_major} = %{version}

%description -n dotnet-runtime-%{dotnet_major}-bin
!!!  This is the Dotnet SDK intended for build pipelines. If you want
to install Dotnet for a development environment, you should install
'dotnet-runtime-%{dotnet_major}' instead.

%package     -n aspnetcore-runtime-%{dotnet_major}-bin
Version:        %{runtime_version}
Summary:        ASP.NET Core %{runtime_version} runtime
Requires:       dotnet-runtime-%{dotnet_major}-bin%{?_isa} >= %{runtime_version}-%{release}
Provides:       aspnetcore-runtime-%{dotnet_major} = %{version}

%description -n aspnetcore-runtime-%{dotnet_major}-bin
!!!  This is the Dotnet SDK intended for build pipelines. If you want
to install Dotnet for a development environment, you should install
'aspnetcore-runtime-%{dotnet_major}' instead.

%package     -n dotnet-templates-%{dotnet_major}-bin
Version:        %{runtime_version}
Summary:        .NET %{runtime_version} templates
# Theoretically any version of the host should work. But lets aim for the one
# provided by this package, or from a newer version of .NET
Requires:       dotnet-host-bin%{?_isa} >= %{runtime_version}-%{release}
Provides:       dotnet-templates-%{dotnet_major} = %{version}

%description -n dotnet-templates-%{dotnet_major}-bin
!!!  This is the Dotnet SDK intended for build pipelines. If you want
to install Dotnet for a development environment, you should install
'dotnet-templates-%{dotnet_major}' instead.

%package     -n dotnet-sdk-%{dotnet_major}-bin
Version:        %{runtime_version}
Summary:        .NET %{runtime_version} SDK
Requires:       dotnet-runtime-%{dotnet_major}-bin%{?_isa} >= %{runtime_version}-%{release}
Requires:       aspnetcore-runtime-%{dotnet_major}-bin%{?_isa} >= %{runtime_version}-%{release}
Requires:       dotnet-apphost-pack-%{dotnet_major}-bin%{?_isa} >= %{runtime_version}-%{release}
Requires:       dotnet-targeting-pack-%{dotnet_major}-bin%{?_isa} >= %{runtime_version}-%{release}
Requires:       aspnetcore-targeting-pack-%{dotnet_major}-bin%{?_isa} >= %{runtime_version}-%{release}
Requires:       dotnet-templates-%{dotnet_major}-bin%{?_isa} >= %{runtime_version}-%{release}
Provides:       dotnet-sdk-%{dotnet_major} = %{version}

%description -n dotnet-sdk-%{dotnet_major}-bin
!!!  This is the Dotnet SDK intended for build pipelines. If you want
to install Dotnet for a development environment, you should install
'dotnet-sdk-%{dotnet_major}' instead.

%package     -n dotnet-sdk-aot-%{dotnet_major}-bin
Version:        %{sdk_version}
Summary:        .NET %{dotnet_major} SDK - Native AoT Support
Requires:       dotnet-sdk-%{dotnet_major}-bin%{?_isa} >= %{runtime_version}-%{release}
# When installing AOT support, also install all dependencies needed to build
# NativeAOT applications. AOT invokes `clang ... -lssl -lcrypto -lbrotlienc
# -lbrotlidec -lz ...`.
Requires:       brotli-devel%{?_isa}
Requires:       clang%{?_isa}
Requires:       openssl-devel%{?_isa}
Requires:       zlib-ng-devel%{?_isa}
Provides:       dotnet-sdk-aot-%{dotnet_major} = %{version}

%description -n dotnet-sdk-aot-%{dotnet_major}-bin
!!!  This is the Dotnet SDK intended for build pipelines. If you want
to install Dotnet for a development environment, you should install
'dotnet-sdk-aot-%{dotnet_major}' instead.

%package     -n dotnet-apphost-pack-%{dotnet_major}-bin
Version:        %{runtime_version}
Summary:        .NET %{dotnet_major} AppHost Pack
Requires:       dotnet-host-bin%{?_isa}
Provides:       dotnet-apphost-pack-%{dotnet_major} = %{version}

%description -n dotnet-apphost-pack-%{dotnet_major}-bin
!!!  This is the Dotnet SDK intended for build pipelines. If you want
to install Dotnet for a development environment, you should install
'dotnet-apphost-pack-%{dotnet_major}' instead.

%package     -n dotnet-targeting-pack-%{dotnet_major}-bin
Version:        %{runtime_version}
Summary:        .NET %{dotnet_major} Targeting Pack
Requires:       dotnet-host-bin%{?_isa}
Provides:       dotnet-targeting-pack-%{dotnet_major} = %{version}

%description -n dotnet-targeting-pack-%{dotnet_major}-bin
!!!  This is the Dotnet SDK intended for build pipelines. If you want
to install Dotnet for a development environment, you should install
'dotnet-targeting-pack-%{dotnet_major}' instead.

%package     -n aspnetcore-targeting-pack-%{dotnet_major}-bin
Version:        %{aspnetcore_runtime_version}
Summary:        ASP.NET Core %{dotnet_major} Targeting Pack
Requires:       dotnet-host-bin%{?_isa}
Provides:       aspnetcore-targeting-pack-%{dotnet_major} = %{version}

%description -n aspnetcore-targeting-pack-%{dotnet_major}-bin
!!!  This is the Dotnet SDK intended for build pipelines. If you want
to install Dotnet for a development environment, you should install
'aspnetcore-targeting-pack-%{dotnet_major}' instead.

%package     -n dotnet-sdk-%{dotnet_major}-source-built-artifacts-bin
Version:        %{sdk_version}
Summary:        .NET %{dotnet_major} Source Built Artifacts
Provides:       dotnet-sdk-%{dotnet_major}-source-built-artifacts = %{version}

%description -n dotnet-sdk-%{dotnet_major}-source-built-artifacts-bin
!!!  This is the Dotnet SDK intended for build pipelines. If you want
to install Dotnet Artifacts for a bootstrap environment, you should install
'dotnet-sdk-%{dotnet_major}-source-built-artifacts' instead.

%prep

%build

%install
install -dm 0755 %{buildroot}%{_libdir}/dotnet
tar xf %{_sourcedir}/dotnet-sdk-%{dotnet_version}-linux-%{runtime_arch}.tar.gz -C %{buildroot}%{_libdir}/dotnet/

%if %{dotnet_is_latest}
install -dm 0755 %{buildroot}%{_bindir}
ln -s ../../%{_libdir}/dotnet/dotnet %{buildroot}%{_bindir}/
ln -s ../../%{_libdir}/dotnet/dnx %{buildroot}%{_bindir}/

install -dm 0755 %{buildroot}%{_sysconfdir}/dotnet
echo "%{_libdir}/dotnet" >> install_location
install install_location %{buildroot}%{_sysconfdir}/dotnet/
echo "%{_libdir}/dotnet" >> install_location_%{runtime_arch}
install install_location_%{runtime_arch} %{buildroot}%{_sysconfdir}/dotnet/
%endif

install -dm 0755 %{buildroot}%{_libdir}/dotnet/source-built-artifacts
install -m 0644 %{_sourcedir}/Private.SourceBuilt.Artifacts.*%{runtime_arch}.tar.gz %{buildroot}/%{_libdir}/dotnet/source-built-artifacts/

find %{buildroot}%{_libdir}/dotnet/shared/Microsoft.NETCore.App -type f -and -not -name '*.pdb' | sed -E 's|%{buildroot}||' > dotnet-runtime-non-dbg-files
find %{buildroot}%{_libdir}/dotnet/shared/Microsoft.NETCore.App -type f -name '*.pdb' -delete
find %{buildroot}%{_libdir}/dotnet/shared/Microsoft.AspNetCore.App -type f -and -not -name '*.pdb' | sed -E 's|%{buildroot}||' > aspnetcore-runtime-non-dbg-files
find %{buildroot}%{_libdir}/dotnet/shared/Microsoft.AspNetCore.App -type f -name '*.pdb' -delete
find %{buildroot}%{_libdir}/dotnet/sdk -type d | tail -n +2 | sed -E 's|%{buildroot}||' | sed -E 's|^|%dir |' > dotnet-sdk-non-dbg-files
find %{buildroot}%{_libdir}/dotnet/sdk -type f -and -not -name '*.pdb' | sed -E 's|%{buildroot}||' >> dotnet-sdk-non-dbg-files
find %{buildroot}%{_libdir}/dotnet/sdk -type f -name '*.pdb' -delete

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
%files -n dotnet-host-bin
%dir %{_libdir}/dotnet
%{_libdir}/dotnet/dotnet
%{_libdir}/dotnet/dnx
%dir %{_libdir}/dotnet/host
%dir %{_libdir}/dotnet/host/fxr
%{_bindir}/dotnet
%{_bindir}/dnx
%license %{_libdir}/dotnet/LICENSE.txt
%license %{_libdir}/dotnet/ThirdPartyNotices.txt
%config(noreplace) %{_sysconfdir}/dotnet
%endif

%files -n dotnet-hostfxr-%{dotnet_major}-bin
%dir %{_libdir}/dotnet/host/fxr
%{_libdir}/dotnet/host/fxr/%{hostfxr_version}*

%files -n dotnet-runtime-%{dotnet_major}-bin -f dotnet-runtime-non-dbg-files
%dir %{_libdir}/dotnet/shared
%dir %{_libdir}/dotnet/shared/Microsoft.NETCore.App
%dir %{_libdir}/dotnet/shared/Microsoft.NETCore.App/%{runtime_version}*

%files -n aspnetcore-runtime-%{dotnet_major}-bin -f aspnetcore-runtime-non-dbg-files
%dir %{_libdir}/dotnet/shared
%dir %{_libdir}/dotnet/shared/Microsoft.AspNetCore.App
%dir %{_libdir}/dotnet/shared/Microsoft.AspNetCore.App/%{aspnetcore_runtime_version}*

%files -n dotnet-templates-%{dotnet_major}-bin
%dir %{_libdir}/dotnet/templates
%{_libdir}/dotnet/templates/%{templates_version}*

%files -n dotnet-sdk-%{dotnet_major}-bin -f dotnet-sdk-non-dbg-files
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

%files -n dotnet-sdk-aot-%{dotnet_major}-bin
%dir %{_libdir}/dotnet/packs
%dir %{_libdir}/dotnet/packs/runtime.%{runtime_id}.Microsoft.DotNet.ILCompiler/
%{_libdir}/dotnet/packs/runtime.%{runtime_id}.Microsoft.DotNet.ILCompiler/%{runtime_version}*
%dir %{_libdir}/dotnet/packs/Microsoft.NETCore.App.Runtime.NativeAOT.%{runtime_id}/
%{_libdir}/dotnet/packs/Microsoft.NETCore.App.Runtime.NativeAOT.%{runtime_id}/%{runtime_version}*
%ifarch riscv64
%dir %{_libdir}/dotnet/packs/Microsoft.NETCore.App.Crossgen2.%{runtime_id}/
%{_libdir}/dotnet/packs/Microsoft.NETCore.App.Crossgen2.%{runtime_id}/%{runtime_version}*
%endif

%files -n dotnet-apphost-pack-%{dotnet_major}-bin
%dir %{_libdir}/dotnet/packs
%{_libdir}/dotnet/packs/Microsoft.NETCore.App.Host.%{runtime_id}

%files -n dotnet-targeting-pack-%{dotnet_major}-bin
%dir %{_libdir}/dotnet/packs
%{_libdir}/dotnet/packs/Microsoft.NETCore.App.Ref

%files -n aspnetcore-targeting-pack-%{dotnet_major}-bin
%dir %{_libdir}/dotnet/packs
%{_libdir}/dotnet/packs/Microsoft.AspNetCore.App.Ref

%files -n dotnet-sdk-%{dotnet_major}-source-built-artifacts-bin
%dir %{_libdir}/dotnet
%{_libdir}/dotnet/source-built-artifacts

%changelog
%autochangelog
