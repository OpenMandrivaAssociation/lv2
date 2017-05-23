%define debug_package %{nil}

Name:		lv2
Version:	1.14.0
Release:	1
Summary:	Audio Plugin Standard
Group:		System/Libraries

# lv2specgen template.html is CC-AT-SA
License:	ISC
URL:		http://lv2plug.in
Source0:	http://lv2plug.in/spec/lv2-%{version}.tar.bz2
Source1:	lv2.rpmlintrc

# this package replaces lv2core
Provides:	lv2core = 6.0-4
Obsoletes:	lv2core < 6.0-4
Provides:	lv2-ui = 2.4-5
Obsoletes:	lv2-ui < 2.4-5

%description
LV2 is a standard for plugins and matching host applications, mainly
targeted at audio processing and generation.

There are a large number of open source and free software synthesis
packages in use or development at this time. This API ('LV2') attempts
to give programmers the ability to write simple 'plugin' audio
processors in C/C++ and link them dynamically ('plug') into a range of
these packages ('hosts').  It should be possible for any host and any
plugin to communicate completely through this interface.

LV2 is a successor to LADSPA, created to address the limitations of
LADSPA which many hosts have outgrown.

%package devel
Summary:	API for the LV2 Audio Plugin Standard
Group:		Development/C

Requires:	%{name} = %{EVRD}
Provides:	lv2core-devel = %{EVRD}
Provides:	lv2-ui-devel = %{EVRD}

BuildRequires:	pkgconfig(sndfile) >= 1.0.0

%description devel
lv2-devel contains the lv2.h header file and headers for all of the
LV@ specification extensions and bundles.

Definitive technical documentation on LV2 plug-ins for both the host
and plug-in is contained within copious comments within the lv2.h
header file.

%prep
%setup -q

%build
%{__python2} ./waf configure -vv --prefix=%{_prefix} --libdir=%{_libdir} --debug --no-plugins --lv2dir=%{_libdir}/%{name} CC=%{__cc}
%{__python2} ./waf -vv %{?_smp_mflags}

%install
DESTDIR=%{buildroot} %{__python2} ./waf -vv install

%files
%{_libdir}/%{name}/*/*.[ch]
%{_libdir}/%{name}/*/*.ttl

%files devel
%doc COPYING NEWS
%{_bindir}/lv2specgen.py
%{_includedir}/%{name}.h
%{_includedir}/%{name}/
%{_datadir}/lv2specgen/
%{_libdir}/pkgconfig/lv2core.pc
%{_libdir}/pkgconfig/%{name}.pc
