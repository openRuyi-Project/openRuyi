# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Han Gao <gaohan@iscas.ac.cn>
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Hangfan Li <lihangfan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%ifarch riscv64
%bcond dtbs  1
%else
%bcond dtbs  0
%endif
%bcond tools 1
%bcond rust  1

# Overrides /usr/lib/rpm/openruyi/macros
%global _lto_cflags %{nil}

# Making flavored kernels by setting this one.
# This will be included into `uname -r` so that multiple kernels will co-exist
%global variant_name %nil

# Managed under kernel-team-tools
%global patchset_release 3
%global config_version 1
# Initial mainline tarballs omit the .0 that the kernel Makefile reports.
%global upstream_version 7.2

Name:           linux
Version:        7.2.0
Release:        %{patchset_release}.%{config_version}_%autorelease
Summary:        The Linux Kernel
License:        GPL-2.0-only
URL:            https://www.kernel.org/
#!RemoteAsset:  sha256:f9fef3d14c0df53819026f4be74459835c2a0b0dcbf5b5bbd9ea19f0829402b3
Source0:        https://cdn.kernel.org/pub/linux/kernel/v7.x/linux-%{upstream_version}.tar.xz
#!RemoteAsset:  sha256:fde1cb23bfaa54c5aa50811eb7462119f1403834a343d8a10e62fac32db54e60
Source1:        https://github.com/openRuyi-Project/kernel-team-tools/releases/download/v%{upstream_version}-%{patchset_release}.%{config_version}/%{name}-v%{upstream_version}-%{patchset_release}.tar.gz

BuildSystem:    linux
# Extracted within %%prep
BuildOption(conf):  %{_sourcedir}/defconfig

BuildRequires:  openruyi-linux-build
%linux_package_dependencies

%if %{with tools}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  clang
BuildRequires:  libtool
BuildRequires:  pkgconfig(babeltrace)
BuildRequires:  pkgconfig(capstone)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libtraceevent)
BuildRequires:  pkgconfig(numa)
BuildRequires:  python3dist(setuptools)
BuildRequires:  systemtap-sdt-devel
%endif

%if %{with rust}
BuildRequires:  bindgen
BuildRequires:  cargo
BuildRequires:  rust
%endif

%description
This is the meta package that handles standard %{name} kernel installation.

%if %{with tools}
%package        tools
Summary:        Set of tools for the %{name} kernel
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-only
Provides:       perf = %{version}-%{release}
Obsoletes:      perf < %{version}-%{release}

%description    tools
This package contains the tools/ directory from the kernel source
and the supporting documentation.

%package        tools-devel
Summary:        Development files for %{name}
License:        GPL-2.0-only
Requires:       %{name}-tools%{?_isa} = %{version}-%{release}

%description    tools-devel
This package contains the libraries and header files for the
tools/ directory from the kernel source.
%endif

%prep
%setup -n %{name}-%{upstream_version}
patchset_dir=.openruyi-patchset
mkdir "${patchset_dir}"
tar -xf "%{SOURCE1}" -C "${patchset_dir}"
while IFS= read -r patch_name; do
    echo "Applying patch: ${patch_name}"
    patch -p1 < "${patchset_dir}/${patch_name}" || exit 1
done < "${patchset_dir}/series"

%if "%{?openruyi_riscv_arch}" == "-march=rva20u64"
    %define arch_suffix -rva20
%else
    %define arch_suffix -generic
%endif
cp -v "${patchset_dir}/config.%{_arch}%{arch_suffix}" %{_sourcedir}/defconfig

%build -a
%if %{with tools}
%make_build -C tools bootconfig gpio iio spi tmon perf
%make_build -C tools/power/cpupower CPUFRQ_BENCH=false VERSION=%{version}

pushd tools/usb/usbip
./autogen.sh
%configure --disable-static
%make_build
popd
%endif

%install -a
%if %{with tools}
# install tools
%make_build -C tools/power/cpupower DESTDIR=%{buildroot} libdir=%{_libdir} mandir=%{_mandir} CPUFREQ_BENCH=false VERSION=%{version} install
%make_build -C tools DESTDIR=%{buildroot} bootconfig_install gpio_install iio_install spi_install
%make_build -C tools INSTALL_ROOT=%{buildroot} tmon_install
%make_build -C tools/perf DESTDIR=%{buildroot} prefix=%{_prefix} install-bin
%make_build -C tools/usb/usbip DESTDIR=%{buildroot} install
find %{buildroot}%{_libdir} -type f -name "*.a" -delete -print
%find_lang cpupower --generate-subpackages
%endif

%if %{with tools}
%files tools -f cpupower.lang
%license COPYING
%config %{_sysconfdir}/cpupower-service.conf
%{_bindir}/bootconfig
%{_bindir}/cpupower
%{_bindir}/gpio-*
%{_bindir}/iio_event_monitor
%{_bindir}/iio_generic_buffer
%{_bindir}/lsgpio
%{_bindir}/lsiio
%{_bindir}/perf
%{_bindir}/spidev_*
%{_bindir}/tmon
%{_bindir}/trace
%{_datadir}/bash-completion/completions/cpupower
%{_libdir}/libcpupower.so*.1
%{_libdir}/libusbip.so.0*
%{_libexecdir}/cpupower
%{_libexecdir}/perf-core
%{_mandir}/man1/cpupower*
%{_mandir}/man8/usbip.8*
%{_mandir}/man8/usbipd.8*
%{_sbindir}/usbip
%{_sbindir}/usbipd
%{_sysconfdir}/bash_completion.d/perf
%{_unitdir}/cpupower.service

%files tools-devel
%dir %{_includedir}/perf
%dir %{_includedir}/usbip
%{_docdir}/perf-tip/tips.txt
%{_includedir}/cpufreq.h
%{_includedir}/cpuidle.h
%{_includedir}/perf/perf_dlfilter.h
%{_includedir}/powercap.h
%{_includedir}/usbip/*.h
%{_libdir}/libcpupower.so
%{_libdir}/libusbip.so
%endif

%linux_package_implementation

%changelog
%autochangelog
